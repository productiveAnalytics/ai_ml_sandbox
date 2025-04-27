# app.py (Stremlit)
import streamlit as st
from data_load import load_document_from_streaming_pdf
from que_and_ans_chain import build_QandA_chain

st.title("📄 AI-Powered Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    loaded_pdf_as_docs = load_document_from_streaming_pdf(uploaded_file)
    st.success("PDF loaded successfully.")

    question_text = st.text_input("Ask a question about the document:")
    if question_text:
        with st.spinner("Thinking..."):
            q_and_a_chain = build_QandA_chain(docs=loaded_pdf_as_docs)
            response = q_and_a_chain(context="Only use the provided documents", question=question_text)
            st.markdown(f"**Answer:** {response}")
