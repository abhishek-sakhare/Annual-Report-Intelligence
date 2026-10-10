
# PDF Intelligence — RAG Application

An AI-powered application that allows users to upload PDF documents and ask questions about their contents.

## Features
- Upload PDF documents
- Extract and split document text into chunks
- Generate embeddings using Sentence Transformers
- Retrieve relevant passages using FAISS
- Generate context-based answers using Google's Gemini API
- Simple interactive interface built with Streamlit

## Tech Stack
- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini API
- PyPDF

## Setup

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file in the project root and add:

   `RAG_API_KEY=your_gemini_api_key`

5. Start the application:

   `streamlit run app.py`

## How to Use
1. Upload a text-based PDF.
2. Enter a question about the document.
3. Click Ask to receive an answer based on the retrieved passages.
