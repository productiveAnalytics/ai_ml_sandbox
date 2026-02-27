from dotenv import load_dotenv
import time
import asyncio

from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage

# LLM_MODEL:str = 'gemini-2.0-flash' # This old model is not available in Google AI studio now!
LLM_MODEL:str = 'gemini-2.5-flash'
llm = None

def initialize_llm_emv() -> bool:

    # initialize environment variables
    load_dotenv()

    global llm
    try:
        llm = GoogleGenAI(model=LLM_MODEL)
        return True
    except Exception as e:
        print(f"ERROR: Failed to initialize LLM model: {LLM_MODEL}")
        print(e)
        return False

### Non-Streaming logic starts ###

def simple_complete(query_txt:str) -> str:
    # LLM sync call
    resp = llm.complete(query_txt)
    return resp
    
async def async_complete(query_txt:str) -> str:
    # LLM async call
    resp = await llm.acomplete(query_txt)
    return resp

def llm_complete__nonstreaming(query_txt:str, mode:str='sync') -> None:
    """
    Query to LLM in non-streaming mode
    """
    start_time_nonstreaming = time.perf_counter()
  
    if mode == 'async':
        query_resp = asyncio.run(async_complete(query_txt=query_txt))
    else:
        query_resp = simple_complete(query_txt=query_txt)

    print(str(query_resp))

    end_time_nonstreaming = time.perf_counter()
    print("\n")
    print(f"Total time (non-streaming): {end_time_nonstreaming - start_time_nonstreaming} seconds")
    print("\n")

### Non-Streaming logic ends ###

###### Streaming logic starts ######

def simple_streaming_complete(query_txt:str) -> None:
    # LLM sync streaming call
    stream_resp = llm.stream_complete(query_txt)
    for chunk in stream_resp:
        print(chunk, end='', flush=True)

async def async_streaming_complete(query_txt:str) -> None:
    # LLM sync non-streaming call
    stream_resp = await llm.astream_complete(query_txt)
    async for chunk in stream_resp:
        print(chunk, end='', flush=True)
 
def llm_complete__streaming(query_txt:str, mode:str='sync') -> None:
    """
    Query to LLM in streaming mode
    """
    start_time_streaming = time.perf_counter()
  
    if mode == 'async':
        asyncio.run(async_streaming_complete(query_txt=query_txt))
    else:
        simple_streaming_complete(query_txt=query_txt)

    end_time_streaming = time.perf_counter()
    print("\n")
    print(f"Total time (streaming): {end_time_streaming - start_time_streaming} seconds")
    print("\n")

###### Streaming logic ends ######

######### Conversaction chat logic starts #########

def llm_chat(streaming_mode:bool=False) -> str:
    """
    Chat with LLM
    """
    start_time_chat = time.perf_counter() 
    messages = [
        ChatMessage(role="user", content="Hello Travel specialist!"),
        ChatMessage(role="assistant", content="Where do you would like to go?"),
        ChatMessage(role="user", content="Help me decide a serene beach holiday destination in India. Only provide max 3 options.")
    ]

    if streaming_mode:
        stream_chat_resp = llm.stream_chat(messages)
        for chunk in stream_chat_resp:
            print(chunk, end='', flush=True)
    else:
        simple_chat_resp = llm.chat(messages)
        print(str(simple_chat_resp))

    end_time_chat = time.perf_counter()
    print("\n")
    print(f"Total chat time ({ 'streaming' if streaming_mode else 'non-streaming' }): {end_time_chat - start_time_chat} seconds")
    print("\n")
    
######### Conversaction chat logic ends #########

def main():
    if not initialize_llm_emv():
        return

    while True:
        print(f"Various LLM apps using llamaindex and model: {LLM_MODEL}")
        print("1. Query (basic)")
        print("2. Query (Asynchronous)")
        print("3. Query (Streaming)")
        print("4. Query (Asynchronous Streming))")
        print("5. Conversational chat (basic)")
        print("6. Conversational chat (streaming)")
        print("0: Exit!")

        program_input = int(input())
        if program_input == 0:
            print("Bye!")
            break

        chat_query:str = "Write a haiku about a Agentic AI"

        next_word_query:str = "The story of Sourcrust, the bread creature, is really interesting. It all started when..."

        if program_input == 1:
            llm_complete__nonstreaming(query_txt=chat_query, mode='sync')
            print("\n")
        elif program_input == 2:
            llm_complete__nonstreaming(query_txt=chat_query, mode='async')
            print("\n")
        elif program_input == 3:
            llm_complete__streaming(query_txt=next_word_query, mode='sync')
            print("\n")
        elif program_input == 4:
            llm_complete__streaming(query_txt=next_word_query, mode='async')
            print("\n")
        elif program_input == 5:
            llm_chat(streaming_mode=False)
            print("\n")
        elif program_input == 6:
            llm_chat(streaming_mode=True)
            print("\n")


if __name__ == "__main__":
    main()
