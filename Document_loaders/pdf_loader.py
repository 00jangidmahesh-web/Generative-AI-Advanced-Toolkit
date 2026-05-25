from langchain_community.document_loaders import TextLoader, PyPDFLoader


loader = PyPDFLoader('pdf_file.pdf')

text = loader.load()

print(text)