import data_load as DL
import que_and_ans_chain as QandA

# Project specific configurations
from conf import *

TEST_DOCUMENTS_PATH:str = "./documents"   # local folder

def create_test_documents():
    loaded_files_and_docs = DL.load_documents_from_folder(documents_folder_path=TEST_DOCUMENTS_PATH)
    
    test_documents = []

    for dict_item in loaded_files_and_docs:
        loaded_docs = dict_item['documents']
        test_documents.extend(loaded_docs)

    return test_documents

def test__QandA():
    test_docs = create_test_documents()
    qa_chain = QandA.build_QandA_chain(docs=test_docs)

    que_text = "What is the main topic of the Berkeley AI Graduate Certificate?"
    # result = qa_chain.invoke({"context": STANDARD_CONTEXT, "question": que_text, "query": que_text})
    result = qa_chain.invoke({"query": que_text})
    print(f"Question: {que_text}")
    print(f"Answer: {result['result']}")

    # que_text = "Can you summarize the key points of the second document?"
    ### result = qa_chain.invoke({"context": STANDARD_CONTEXT, "question": que_text})
    # result = qa_chain.invoke({"query": que_text})
    # print(f"\nQuestion: {que_text}")
    # print(f"Answer: {result['result']}")