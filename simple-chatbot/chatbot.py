from langchain.chat_models import init_chat_model

from langchain_core.prompts import ChatPromptTemplate

import getpass
import os

API_KEY_NAME = "GOOGLE_API_KEY"
MODEL_NAME = "gemini-2.0-flash-lite"

def configure_api_key(mode:str = 'cli', api_key:str = None) -> None:
    """
    Sets the API key

        mode: cli
            Allows to read key from promt if not set

        mode: ui
            Streamlit app needs to send the key
    """
    if not os.environ.get(API_KEY_NAME):
        if mode == 'cli':
            genai_api_key = getpass.getpass("Enter API key for Google Gemini: ")
        else:
            genai_api_key = api_key

        assert len(genai_api_key) > 0

        print(genai_api_key)
        os.environ[API_KEY_NAME] = genai_api_key
    else:
        print(f"{API_KEY_NAME} is available as env variable")

def initialize_genai():
    """
    Must be called only once in application lifecycle
    Returns model and prompt template
    """
    model = init_chat_model(MODEL_NAME, model_provider="google_genai")

    system_template = "Translate the following from English into {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_template), 
            ("user", "{text}")
        ]
    )

    return model, prompt_template

def launch_chat_app(model, prompt_template, user_language:str, user_text:str) -> str:


    prompt = prompt_template.invoke({"language": user_language, "text": user_text})

    response = model.invoke(prompt)
    response_from_genai = response.content

    return response_from_genai