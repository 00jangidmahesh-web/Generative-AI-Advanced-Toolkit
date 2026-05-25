# it generate a 32 dimention vector, jo simantic meaning capture kar rha hoga given sentence ka
# used in ----> RAG etc.. only related part of data ko select karne me help karta hai

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
# dimension = 32 means the entire sentence is represented by 32 numbers

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))