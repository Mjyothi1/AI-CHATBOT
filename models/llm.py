from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY

def get_chatgroq_model():
    try:
        model = ChatGroq(
            api_key="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",
            model="llama-3.1-8b-instant"
        )
        return model

    except Exception as e:
        raise RuntimeError(f"LLM error: {str(e)}")
