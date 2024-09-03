from langchain_groq import ChatGroq

from config import load_config, get_groq_api_key


# Function to setup the llm
def groq_llm():
    llm = ChatGroq(
        model='gemma2-9b-it',
        temperature=0.7,
        api_key=get_groq_api_key()
    )
    return llm