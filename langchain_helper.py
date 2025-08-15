import io
import re
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()


def _extract_text_from_pdf(uploaded_file, start_page_1b, end_page_1b):
    data = uploaded_file.getvalue()
    reader = PdfReader(io.BytesIO(data))
    total_pages = len(reader.pages)
    start = max(0, min(total_pages - 1, start_page_1b - 1))
    end = max(0, min(total_pages - 1, end_page_1b - 1))

    if end < start:
        raise ValueError("Ending page is before starting page.")

    page_texts = []
    for i in range(start, end + 1):
        txt = reader.pages[i].extract_text() or ""
        page_texts.append(txt)

    text = "\n".join(page_texts)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text).strip()
    return text, total_pages


def generate_summary(pdf_file, starting_page_number, ending_page_number, number_of_paragraphs, number_of_sentences):
    page_text, total = _extract_text_from_pdf(pdf_file, starting_page_number, ending_page_number)
    if not page_text:
        raise ValueError(
            "No text extracted from the selected pages. "
            "Try a different range or ensure the PDF is text-based (not scanned)."
        )

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.5)

    prompt = PromptTemplate(
        input_variables=["page_text", "num_paragraphs", "num_sentences"],
        template=(
            "You are a precise summarizer. Obey these constraints EXACTLY:\n"
            "- Output exactly {num_paragraphs} paragraphs.\n"
            "- Each paragraph has at exactly {num_sentences} sentences.\n"
            "- No bullet points; use plain paragraphs.\n"
            "- Summarize only what appears in the text; do not add facts.\n\n"
            "TEXT START\n{page_text}\nTEXT END"
        )
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke(
        {
            "page_text": page_text,
            "num_paragraphs": str(number_of_paragraphs),
            "num_sentences": str(number_of_sentences),
        }
    )
    if isinstance(result, dict) and "text" in result:
        return result["text"]
    return str(result)
