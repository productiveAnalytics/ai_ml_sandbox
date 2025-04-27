# que_and_ans_chain.py
###from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
###from langchain.llms import HuggingFacePipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

import torch

import os

# Project specific configurations
from conf import *


# Build retrieval + QA chain using ChromaDB
def build_QandA_chain(docs, persist_directory="chroma_store"):
    # Embeddings model
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # Persistent vector store
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_directory)
    # vectorstore.persist()  # Save the vectors

    # Use a pipeline as a high-level helper
    q_and_a_pipeline = pipeline("document-question-answering", model=LLM_MODEL)


    # Question-Answering LLM
    llm = HuggingFacePipeline(pipeline=q_and_a_pipeline)

    prompt_template = PromptTemplate(
        template=PROMPT_TEXT_TEMPLATE,
        input_variables=["context", "question"],
        validate_template=True
    )

    retriever = vectorstore.as_retriever()

    # q_and_a_chain = RetrievalQA.from_chain_type(
    #     verbose=False,
    #     llm=llm, 
    #     chain_type="stuff", 
    #     retriever=retriever,
    #     chain_type_kwargs={"prompt": prompt_template}
    # )
    q_and_a_chain = RetrievalQA.from_chain_type(
        verbose=True,
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever
    )

    return q_and_a_chain
