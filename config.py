import os
from dotenv import load_dotenv

def get_groq_key():
    """
    get_groq_key

    Gets the environment variable from .env file containing the GROQ_KEY variable.
    This API key can be acquired from https://console.groq.com/keys

    :return: Groq API Key
    """
    load_dotenv()
    return os.environ.get("GROQ_KEY")