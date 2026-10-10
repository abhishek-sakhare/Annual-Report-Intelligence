# 📊 Company Annual Report Intelligence & Analytics

A **Retrieval-Augmented Generation (RAG)** application that allows users to interact with company annual reports using natural-language questions. The system retrieves relevant information from unstructured PDF documents and uses an LLM to generate context-grounded responses.

## 🚀 Project Overview

Company annual reports contain large amounts of financial, operational, and strategic information spread across hundreds of pages. Manually searching through these documents can be time-consuming.

This project uses **RAG** to make annual reports easier to explore. Users can upload or query annual reports and ask questions such as:

- What was the company's revenue?
- What are the major business segments?
- What were the company's key risks?
- What are the company's future strategies?
- What were the major expenses?
- How did the company's performance change?

The application retrieves relevant sections from the reports and provides answers based on the retrieved context.

## 🔄 How It Works

```text
Annual Report (PDF)
        ↓
   Text Extraction
        ↓
    Text Chunking
        ↓
    Embeddings
        ↓
   FAISS Vector Store
        ↓
    User Question
        ↓
Semantic Similarity Search
        ↓
 Relevant Document Chunks
        ↓
       LLM
        ↓
 Context-Grounded Answer
```

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** combines information retrieval with a Large Language Model.

Instead of relying only on the LLM's existing knowledge, the system:

1. Converts document content into smaller chunks.
2. Creates vector embeddings for the chunks.
3. Stores the embeddings in a vector database.
4. Converts the user's question into an embedding.
5. Retrieves the most relevant document chunks.
6. Provides the retrieved context to the LLM.
7. Generates an answer based on the retrieved information.

This helps the application answer questions using the information contained in the uploaded annual reports.

## 🛠️ Technologies Used

- **Python** — Core programming and data processing
- **Pandas** — Data manipulation and analysis
- **PyPDF** — PDF text extraction
- **LangChain** — RAG pipeline components
- **FAISS** — Vector similarity search
- **Embeddings** — Semantic representation of document text
- **LLM** — Context-based answer generation
- **Streamlit** — Interactive web application

## 📁 Project Structure

```text
Annual-Report-Intelligence/
│
├── data/
│   └── annual_reports/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Example Questions

After uploading an annual report, users can ask:

```text
What was the company's total revenue?

What are the company's major business segments?

What risks does the company identify?

What are the company's future growth strategies?

What were the major expenses during the year?
```

## 📈 Data Analytics Extension

The project can also be extended with an analytics layer by recording user queries and application metrics such as:

- Number of queries
- Query categories
- Most frequently accessed reports
- Response time
- Frequently asked questions

These metrics can then be analyzed using **Pandas and Power BI** to identify usage patterns and generate business insights.

## 🎯 Learning Objectives

Through this project, I developed an understanding of:

- Retrieval-Augmented Generation (RAG)
- Text preprocessing and document chunking
- Vector embeddings
- Semantic search
- Vector databases
- LLM-based question answering
- Working with unstructured business documents
- Building interactive data applications with Streamlit

## 🔮 Future Improvements

- Support multiple annual reports simultaneously
- Add source/page references for retrieved information
- Compare financial information across multiple years
- Add automated financial KPI extraction
- Add Power BI analytics for query and document usage
- Improve retrieval using hybrid search and reranking

## 👨‍💻 Author

**Abhishek Sakhare**

B.Tech — Civil Engineering  
NIT Agartala

Interested in **Data Analytics, Business Intelligence, Python, SQL, Power BI, and Generative AI**.
