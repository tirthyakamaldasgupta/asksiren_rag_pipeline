# 🧠 Retrieval-Augmented QA on Siren Craft Brew FAQs

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain and Mistral AI. It loads FAQs from the **Siren Craft Brew** website, vectorizes them, and allows users to ask natural language questions, which are answered using relevant information retrieved from the page.

---

## 📋 Features

- 🔍 Loads FAQ content from a specified webpage
- 🧩 Splits documents into manageable chunks
- 🧠 Embeds and stores the content in memory
- 🤖 Uses `MistralAI` for embeddings and chat completion
- 💬 Answers user queries based on retrieved context
- 🌐 Built using LangChain ecosystem

---

## 🛠️ Tech Stack

- Python 3.9+
- [LangChain](https://www.langchain.com/)
- [MistralAI](https://docs.mistral.ai/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- dotenv for managing secrets

---

## 🚀 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/siren-rag-demo.git
cd siren-rag-demo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file with the following:

```
SIRENCRAFTBREW_FAQS_URL=https://your_faq_page_url
MISTRALAI_API_KEY=your_mistral_api_key
```

> 🔑 Replace `your_faq_page_url` with the actual FAQ page of Siren Craft Brew.  
> Get your Mistral API key from https://console.mistral.ai/

---

## 🧪 Run the App

```bash
python main.py
```

You will be prompted to enter a question like:

```
What is your question? When will my order arrive?
```

And the script will print a well-formatted answer based on retrieved content.

---

## 🧾 How it Works

1. **Document Loading:** Loads the FAQ page using `WebBaseLoader` and BeautifulSoup with filters for specific classes.
2. **Chunking:** Splits long content into smaller chunks for efficient vector storage.
3. **Embedding:** Uses `MistralAIEmbeddings` to convert text to vectors.
4. **Vector Store:** Stores embedded content in an in-memory store.
5. **Retrieval + Generation:** Uses similarity search to retrieve relevant chunks, and feeds them along with the question into a prebuilt RAG prompt from LangChain Hub to generate the answer.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.