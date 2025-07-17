# 🧠 AskSiren RAG Pipeline – FastAPI-powered Retrieval-Augmented QA

This project wraps a Retrieval-Augmented Generation (RAG) pipeline using **LangChain** and **Mistral AI** into a production-ready **FastAPI** server. It allows querying FAQ content from the [Siren Craft Brew](https://www.sirencraftbrew.com/) website via a RESTful API.

---

## 📋 Features

- 🔍 Loads FAQ content from the Siren Craft Brew website
- 🧩 Splits and embeds documents for semantic retrieval
- 🧠 Uses **Mistral AI** for both embeddings and response generation
- 🌐 REST API built using **FastAPI**
- 🔄 Stateless `/ask` endpoint to answer user questions
- ⚡ Auto-generated Swagger docs at `/docs`

---

## 🛠️ Tech Stack

- Python 3.9+
- FastAPI
- LangChain
- Mistral AI
- BeautifulSoup4
- python-dotenv
- uvicorn (for running server)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/asksiren_rag_pipeline.git
cd asksiren_rag_pipeline
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the project root:

```
SIRENCRAFTBREW_FAQS_URL=https://your_faq_page_url
MISTRALAI_API_KEY=your_mistral_api_key
```

> 🔑 Replace `your_faq_page_url` with the actual Siren Craft Brew FAQ page.  
> 🔑 Get your Mistral API key from https://console.mistral.ai/

---

## ▶️ Run the FastAPI App

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🔗 API Usage

### 📥 POST `/ask`

Ask a question and get a context-aware answer from the RAG system.

#### Request (JSON)
```json
{
  "question": "When will my order arrive?"
}
```

#### Response (JSON)
```json
{
  "answer": "We aim to deliver orders within 2-3 working days..."
}
```

You can test using `curl`:

```bash
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question": "When do you ship orders?"}'
```

---

## 🧾 How It Works

1. **Document Loading**: Fetches FAQs from the target webpage using `BeautifulSoup`.
2. **Chunking**: Splits FAQ content into small, manageable blocks.
3. **Embedding**: Converts text chunks into dense vectors using `MistralAIEmbeddings`.
4. **Vector Store**: Stores vectors in memory for fast similarity search.
5. **Retrieval + Generation**: Retrieves top-k relevant chunks and passes them with the query to `ChatMistralAI` using a LangChain RAG prompt template.
6. **Serving**: The entire flow is exposed as a REST API via FastAPI.

---

## 📁 File Structure

```
.
├── main.py               # FastAPI app with /ask endpoint
├── rag_pipeline.py       # Core logic for loading, embedding, and answering
├── requirements.txt      # Python dependencies
├── .env                  # Secrets and config
└── README.md             # Documentation
```

---

## 📘 License

MIT License. See `LICENSE` for more details.
