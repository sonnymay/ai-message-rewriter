import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Message Rewriter", page_icon="💬", layout="centered")

st.title("💬 AI Message Rewriter")
st.write("Rewrite your messages to sound more professional, friendly, or concise.")

text = st.text_area("✍️ Enter your message:", height=150)

tone = st.selectbox(
    "Choose tone:",
    ["Professional", "Friendly", "Concise"]
)

if st.button("Rewrite Message"):
    if not text.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Rewriting..."):
            prompt = f"Rewrite this message in a {tone.lower()} tone: {text}"
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an assistant that rewrites messages politely."},
                    {"role": "user", "content": prompt}
                ],
            )
            rewritten = response.choices[0].message.content.strip()
            st.success("✅ Rewritten message:")
            st.write(rewritten)
