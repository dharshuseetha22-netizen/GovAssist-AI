import streamlit as st
from groq import Groq

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "Say Hello"}
        ],
    )

    st.success("✅ Groq API key is working!")
    st.write(response.choices[0].message.content)

except Exception as e:
    st.error(f"Error: {e}")
