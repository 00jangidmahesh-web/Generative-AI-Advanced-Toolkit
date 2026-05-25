import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

client = InferenceClient(
    model="facebook/bart-large-cnn",
    token=HF_TOKEN
)

st.title("Text Summarization Tool")

text = st.text_area("Enter text")

if st.button("Summarize"):
    result = client.summarization(
        text,
        max_length=150,
        min_length=40
    )
    st.write(result["summary_text"])
