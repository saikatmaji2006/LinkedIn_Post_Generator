import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    """Initialize and return the Groq LLM instance.

    Supports both local (.env) and Streamlit Cloud (st.secrets) API key sources.
    """
    api_key = os.getenv("GROQ_API_KEY")

    # Fallback to Streamlit secrets (for Streamlit Cloud deployment)
    if not api_key:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except (FileNotFoundError, KeyError):
            pass

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Set it in .env or Streamlit secrets."
        )

    return ChatGroq(groq_api_key=api_key, model_name="openai/gpt-oss-120b")


llm = get_llm()

if __name__ == "__main__":
    response = llm.invoke("give me tips to focus on studies (3 most important points)")
    print(response.content)
