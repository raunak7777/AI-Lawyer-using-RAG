import streamlit as st 
from rag_pipeline import answer_query, retrieve_docs, llm_model

# Page configuration
st.set_page_config(
    page_title="LawAI - Your AI Lawyer",
    page_icon="⚖️",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #002855;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">⚖️ LawAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Rosy, your AI lawyer, is here to help. Upload your PDF and ask anything legal.</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📄 Upload a Legal Document (PDF only)", type="pdf")

# Text area for query
user_query = st.text_area(
    "💬 Ask Rosy, your AI Lawyer:", 
    height=150, 
    placeholder="Hey Dear! This is Rosy, your AI Lawyer. Ask Anything!"
)

# Ask button
ask_question = st.button("🔍 Ask AI Lawyer")

# Handle button logic
if ask_question:
    if uploaded_file:
        st.chat_message("user").write(user_query)

        # RAG Pipeline
        with st.spinner("Analyzing your document and generating a response..."):
            retrieved_docs = retrieve_docs(user_query)
            response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

        st.chat_message("AI Lawyer").write(response)
    else:
        st.warning("⚠️ Please upload a PDF file before asking a question.")
