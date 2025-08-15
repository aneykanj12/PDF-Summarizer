# PDF Summarizer 
This is a simple PDF summary page that lets a user see a summary of the file. This program uses the Gemini Flash 1.5 LLM model and I used LangChain to connect everything together. The basic user-interface is done with Streamlit.

## How to Use
Before using the program, since this uses Gemini Flash 1.5, the user needs to generate an API key from <a href="https://console.cloud.google.com/">Google Cloud Console</a>. Make a project, enable gemini, and generate a key. This is model is free :)
To use the program, the user would upload **1** .pdf file in the drop box. Then you can adjust the starting page, ending page, number of paragraphs, and number of sentences. Click the summarize button and you get a summary of the file.
