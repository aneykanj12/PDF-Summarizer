import langchain_helper as lch
import streamlit as st

st.title("PDF Summarizer")
user_pdf_file = st.file_uploader("Upload your PDF file here", type=["pdf"]) 

st.sidebar.header("Controls")
user_starting_page_number = st.sidebar.number_input("What is the starting page number you want to summarize from?", min_value=1, max_value=3000)
user_ending_page_number = st.sidebar.number_input("What is the ending page number you want to summarize to?", min_value=1, max_value=3000)
user_number_of_paragraphs = st.sidebar.number_input("How many paragraphs do you want your summary in?", min_value=1, max_value=1000)
user_number_of_sentences = st.sidebar.number_input("How many sentences do you want for each paragraph?", min_value=1, max_value=10)
render_text = st.sidebar.button("Summarize")

if render_text:
    if not user_pdf_file:
        st.error("You need to upload a PDF file!")
    elif user_starting_page_number > user_ending_page_number:
        st.error("Your starting page number is larger than your ending page number!")
    else:
        if user_pdf_file and user_starting_page_number and user_ending_page_number and user_number_of_paragraphs and user_number_of_sentences:
            with st.spinner("Summarizing..."):
                try:
                    summary_text = lch.generate_summary(
                        user_pdf_file, user_starting_page_number, 
                        user_ending_page_number, 
                        user_number_of_paragraphs, 
                        user_number_of_sentences)
                
                    st.write(summary_text)
                except Exception as e:
                    st.error(f"Error: {e}")