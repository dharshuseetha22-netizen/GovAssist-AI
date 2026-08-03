import streamlit as st
from groq import Groq

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="🏛️ GovAssist AI",
    page_icon="🏛️",
    layout="wide"
)

# -----------------------------
# Groq Client
# -----------------------------
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("❌ GROQ_API_KEY not found in Streamlit Secrets.")
    st.stop()

# -----------------------------
# Header
# -----------------------------
st.title("🏛️ GovAssist AI")
st.subheader("Government Scheme, Scholarship & Funding Finder")

st.markdown("""
Find Government Schemes, Scholarships, Subsidies, Loans and Funding
available in India using Artificial Intelligence.
""")

st.divider()

# -----------------------------
# User Input
# -----------------------------
domain = st.text_input(
    "Enter a Domain",
    placeholder="Example: Agriculture, Education, Medical, Startup, Housing..."
)

state = st.text_input(
    "State (Optional)",
    placeholder="Example: Tamil Nadu, Karnataka..."
)

# -----------------------------
# Search Button
# -----------------------------
if st.button("🔍 Search Schemes", use_container_width=True):

    if domain.strip() == "":
        st.warning("Please enter a domain.")
        st.stop()

    prompt = f"""
You are India's best Government Scheme Expert.

Find every possible REAL Government Scheme related to:

Domain:
{domain}

State:
{state if state else "All India"}

Provide information in the following format.

# Scheme Name

### Ministry / Department

### Central or State Government

### Purpose

### Who Can Apply

### Eligibility

### Benefits

### Funding Amount

### Documents Required

### How to Apply

### Official Government Website

### Last Date (if available)

### Important Notes

Rules:

- Include only genuine Government Schemes.
- Never create fake schemes.
- Include Central Government and State Government schemes.
- Mention if a scheme is state-specific.
- Use markdown headings.
- Mention official government websites only.
"""

    try:

        with st.spinner("Searching Government Schemes..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_completion_tokens=4096,
            )

        result = response.choices[0].message.content

        st.success("✅ Results Found")

        st.markdown(result)

    except Exception as e:
        st.error("❌ Error while fetching results.")
        st.exception(e)

st.divider()

st.caption("🏛️ GovAssist AI | Powered by Streamlit + Groq Llama 3.3")
