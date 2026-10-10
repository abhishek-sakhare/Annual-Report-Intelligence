
import streamlit as st
from rag import process_pdf, get_answer

st.set_page_config(
    page_title="PDF Intelligence",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF Intelligence")

st.caption(
    "An AI-powered assistant to explore any PDF document."
)

st.divider()

# Upload a PDF
uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    try:
        with st.spinner("Processing your PDF..."):
            pdf_bytes = uploaded_file.getvalue()
            chunks, index = process_pdf(pdf_bytes)

        st.subheader("Ask your question")

        st.write(
            "Ask about the document's key information, "
            "figures, findings, or conclusions."
        )

        question = st.text_input(
            "Your question",
            placeholder="What is this document about?"
        )

        if st.button("Ask"):
            if question.strip():
                with st.spinner("Finding the answer..."):
                    try:
                        answer = get_answer(
                            question, chunks, index
                        )
                        st.subheader("Answer")
                        st.write(answer)

                    except Exception:
                        st.error(
                            "Unable to generate an answer. "
                            "Please try again."
                        )
            else:
                st.warning("Please enter a question.")

    except Exception as e:
        st.error(f"Could not process this PDF: {e}")

else:
    st.info("Upload a PDF to get started.")

st.divider()

st.caption(
    "Built with Python, Streamlit, FAISS, "
    "Sentence Transformers and Gemini."
)
