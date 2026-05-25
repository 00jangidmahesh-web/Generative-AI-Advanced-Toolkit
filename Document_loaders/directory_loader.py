from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader


loader = DirectoryLoader(
    path = 'main_folder_path',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

text_of_all_pdf_file = loader.load()

print(text_of_all_pdf_file)

print(len(text_of_all_pdf_file))