import os
from dotenv import load_dotenv, find_dotenv                                                                                                                                   
def load_env():
    _ = load_dotenv(find_dotenv())

def get_ai21_api_key():
    load_env()
    ai21_api_key = os.getenv("AI21_API_KEY")
    return ai21_api_key
