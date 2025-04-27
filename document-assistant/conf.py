CHUNK_SIZE:int = 1014

CHUNK_OVERLAP:int = 96

EMBEDDING_MODEL:str = "sentence-transformers/all-MiniLM-L6-v2"
#EMBEDDING_MODEL:str = "sentence-transformers/all-mpnet-base-v2"

# LLM_MODEL:str = "mistralai/Mistral-7B-Instruct-v0.2"
# LLM_MODEL:str = "distilbert/distilbert-base-cased-distilled-squad"
# LLM_MODEL:str = "google/flan-t5-base"
# LLM_MODEL:str = "meta-llama/Meta-Llama-3-8B-Instruct"
LLM_MODEL:str = "deepset/roberta-base-squad2"

PROMPT_TEXT_TEMPLATE:str = """Use the following context to answer the question.
Context: {context}
Question: {question}
Answer:"""

STANDARD_CONTEXT:str = "ValueError: Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer."