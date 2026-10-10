
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from dotenv import load_dotenv
from google import genai
import os 
from io import BytesIO


model = SentenceTransformer("all-MiniLM-L6-v2")

load_dotenv()
api_key = os.getenv("RAG_API_KEY")

if not api_key:
    raise ValueError("RAG_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

def process_pdf(pdf_bytes):
    reader = PdfReader(BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    if not text.strip():
        raise ValueError("No readable text found in this PDF.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    return chunks, index




def get_answer(question, chunks, index):
    question_embedding = model.encode([question])

    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        5
    )

    retrieved_chunks = [
        chunks[i] for i in indices[0] if i != -1
    ]

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
    Answer the question using only the context below.

    If the answer is not available in the context,
    say that the information was not found in the report.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text





























# # reader = PdfReader("data/annual_reports/tcs-ar.pdf")

# text = ""
# for page in reader.pages:
#     text +=  (page.extract_text() or "") + "\n"
# # print(text[:5000])
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 1000,
#     chunk_overlap  = 200
# )
# chunks = splitter.split_text(text)
# print("Number of Chunks:", len(chunks))
# # for chunk in chunks:
# #     print(chunk)
# #     print("\n---\n")


# embeddings = model.encode(chunks)
# print("Embeddings shape:", embeddings.shape)

# dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings).astype("float32"))
# print("Number of vectors in the index:", index.ntotal)
# 

