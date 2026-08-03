import streamlit as st
import os
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.write(os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="GovAssist AI",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Government Scheme Finder AI")

st.write(
"""
Find Government Schemes, Scholarships and Funding
using Artificial Intelligence.
"""
)

domain = st.text_input(
    "Enter Domain",
    placeholder="Example: Agriculture, Education, Medical, Housing, Startup..."
)

if st.button("Search Schemes"):

    if domain == "":
        st.warning("Enter a domain")
    else:

        prompt = f"""

You are an expert Government Scheme Advisor.

The user entered this domain:

{domain}

Generate every possible Government Scheme available in India.

For each scheme provide:

1. Scheme Name

2. Ministry

3. Purpose

4. Eligibility

5. Benefits

6. Required Documents

7. Registration Process

8. Official Registration Website

9. Application Deadline (if available)

10. Can Everyone Apply?
(Yes/No)

11. State or Central Government

12. Scholarship/Funding Amount

13. Short Summary

Format nicely using markdown headings.

Never create fake schemes.

If unsure, clearly mention it.

"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        result = response.choices[0].message.content

        st.success("Results")

        st.markdown(result)
