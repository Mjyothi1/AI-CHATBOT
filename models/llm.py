from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY

def get_chatgroq_model():
    try:
        model = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant"
        )
        return model

    except Exception as e:
        raise RuntimeError(f"LLM error: {str(e)}")