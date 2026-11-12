import streamlit as st
import requests

st.title("⚡ Gamma App (Qwen 2.5 0.5B)")

user_input = st.text_input("Enter a prompt or message:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            # Call Ollama local API endpoint
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen2.5:0.5b",
                    "prompt": user_input,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                answer = response.json().get("response", "")
                st.write("### AI Response:")
                st.success(answer)
            else:
                st.error(f"Ollama Error: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to connect to Ollama: {e}")
