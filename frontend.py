import streamlit as st 
from rag_pipeline import answer_query, retrieve_docs, llm_model

#UI Skeleton using Streamlit
uploaded_file =  st.file_uploader("Upload PDF",
                                  type="pdf",
                                  accept_multiple_files=False)

user_query = st.text_area("Enter your prompt: ", height=150, placeholder= "Hey Dear! This is Rosy, your AI Lawyer. Ask Anything!")

ask_question = st.button("Ask AI Lawyer")

if ask_question:
    
    if uploaded_file:
        
        st.chat_message("user").write(user_query)
        
        #RAG Pipeline
        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        st.chat_message("AI Lawyer").write(response)
        
    else:
        st.error("Gandu, phele PDF file toh upload kar!!!")
