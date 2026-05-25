from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

docs = PyPDFLoader('My_pdf_file.pdf')

text = docs.load()

splitter = CharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_text(text)

print(result)