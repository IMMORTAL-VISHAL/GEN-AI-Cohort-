from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent / "notes.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

print(docs[10])