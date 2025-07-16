from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


def main():
    llm = init_chat_model(
        "mistral-large-latest",
        model_provider="mistralai"
    )

    embeddings = MistralAIEmbeddings(model="mistral-embed")

    vector_store = InMemoryVectorStore(embeddings)

    response = llm.invoke("Hi. Good morning. How are you today?")

    print(response.content)


load_dotenv()

if __name__ == "__main__":
    main()
