# PDF Summarizer 

## Summary
This is a simple PDF summary page that lets a user see a summary of the file. This program uses the Gemini Flash 1.5 LLM model and I used LangChain to connect everything together. The basic user-interface is done with Streamlit.

## How to Use

### API Key
Before using the program, the user needs to get an API key from Google Cloud Console as the model is Gemini Flash 1.5. You can follow these steps to get the key:
- Head over to <a href="https://console.cloud.google.com/">Google Cloud Console</a>
- You need to make a project, and then choose **API's and Servicees** then **library**
- From there you want to enable the api
- Now in the **API's and Servicees** head over to **Credentials**
- From **Create Credentials**, you want to make an API key
- Copy the key and replace the string in the .env with the key and you are all set.

### How to use the program
These are the directions for how to use the app:
- Now you can see the streamlit hosted in your web browser
- So upload **1** .pdf file into the drop box
- Then adjust the starting page, ending page, paragraph and sentences count
- Finally hit the summarize button and you will see the sumamry of the document
