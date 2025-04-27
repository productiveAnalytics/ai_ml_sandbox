from langchain_community.document_loaders import TextLoader, PDFPlumberLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

import fitz # PyMuPDF

import os

# Project specific configurations
from conf import *

def load_documents_from_folder(documents_folder_path:str) -> list:
    """
    Loads PDF and/or TXT documents from local folder

    Returns the list with ditionary that file path and corresponding loaded Documents
    """
    
    file_and_documents = []
    total_docs:int = 0

    for filename in os.listdir(documents_folder_path):
        documents = []
        file_path = os.path.join(documents_folder_path, filename)
        print(f"file to load: {file_path}")

        if filename.endswith(".txt"):
            txt_loader = TextLoader(file_path)
            documents.extend(txt_loader.load())
        elif filename.endswith(".pdf"):
            pdf_loader = PDFPlumberLoader(file_path)
            documents.extend(pdf_loader.load())

        loaded_docs_as_dict = {"file_path": file_path, "documents": documents}
        total_docs += len(documents)

        file_and_documents.append(loaded_docs_as_dict)


    print(f"Loaded {len(file_and_documents)} files as {total_docs} documents.")

    return file_and_documents


# Split text into chunks
def chunk_text(text:str):
    txt_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = txt_splitter.split_text(text)
    documents = [Document(page_content=chunk) for chunk in chunks]

    print(f"Text of size {len(text)} was loaded as {len(documents)} documents.")
    return documents


def load_document_from_streaming_pdf(pdf_file) -> list:
    """
    Extract the text from the streaming pdf

    Returns list of Documents
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text_from_pdf = ""
    for page in doc:
        text_from_pdf += page.get_text()

    return chunk_text(text=text_from_pdf)
    


# if __name__ == '__main__':
#     test_documents_path = "./documents"
#     test_files_and_docs = load_documents_from_folder(documents_folder_path=test_documents_path)
#     for dict_item in test_files_and_docs:
#         file_name = dict_item['file_path']
#         print(file_name)