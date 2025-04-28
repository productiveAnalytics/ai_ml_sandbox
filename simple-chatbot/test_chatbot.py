from chatbot import *

TEST_LANGUAGE = "Spanish"
TEST_TEXT = "Hello, where is the nearest exit to the street?"

def test__chatbot():
    configure_api_key()

    genai_model, prompt_template = initialize_genai()

    response_txt = launch_chat_app(genai_model, prompt_template, user_language=TEST_LANGUAGE, user_text=TEST_TEXT)

    print(f"English text: {TEST_TEXT}\n")
    print(f"{TEST_LANGUAGE} text: {response_txt}\n")
    assert response_txt