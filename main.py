import os

import bs4
from dotenv import load_dotenv
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import WebBaseLoader
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main():
    question = input("What is your question? ")

    llm = init_chat_model(
        "mistral-large-latest",
        model_provider="mistralai"
    )

    embeddings = MistralAIEmbeddings(model="mistral-embed")

    vector_store = InMemoryVectorStore(embeddings)

    prompt = hub.pull("rlm/rag-prompt")

    loader = WebBaseLoader(
        web_paths=(os.environ["SIRENCRAFTBREW_FAQS_URL"],),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("title", "faqAnswer")
            )
        ),
    )

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20
    )

    all_splits = text_splitter.split_documents(docs)

    _ = vector_store.add_documents(documents=all_splits)

    retrieved_docs = vector_store.similarity_search(question)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    messages = prompt.invoke({"question": question, "context": docs_content})

    response = llm.invoke(messages)

    print(response.content.replace(". ", ".\n"))


load_dotenv()

if __name__ == "__main__":
    main()
