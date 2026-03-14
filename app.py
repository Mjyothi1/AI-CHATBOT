import streamlit as st
from utils.rag import retrieve
from utils.web_search import web_search
from models.llm import get_chatgroq_model
from langchain_core.messages import HumanMessage, SystemMessage

def get_chat_response(chat_model, messages, system_prompt):
    formatted_messages = [SystemMessage(content=system_prompt)]
    for msg in messages:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        # For simplicity in this snippet, appending just the Human messages.
    
    response = chat_model.invoke(formatted_messages)
    return response.content
    
def chat_page():
    st.title("🤖 AI ChatBot")
    mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"]
    )
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            chat_model = get_chatgroq_model()
            
            context = retrieve(prompt)
            web = web_search(prompt)
            
            if mode == "Concise":
                system_prompt = f"Answer briefly. Context: {context} Web: {web}"
            else:
                system_prompt = f"Explain in detail. Context: {context} Web: {web}"
            
            response = get_chat_response(chat_model, st.session_state.messages, system_prompt)
            st.markdown(response)
            
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    chat_page()
