from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# Setup client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=hf_token
)

# Streamlit UI
st.title("🤖 Robo")
user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b:groq",
                messages=[{"role": "user", 
                           "content": user_input
                    }]            
                )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
