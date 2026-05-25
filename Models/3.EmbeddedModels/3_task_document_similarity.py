# using closed-source model

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# document jisme se question puchhenge
document = [
    'my name is Ayush.',
    "im doing my master's from iit dhanbad.",
    "i want to become a ai engineer."
]
docs_emb = embeddings.aembed_documents(document)

query = 'tell me what is the goal of Ayush?'
query_emb = embeddings.embed_query(query)

score = cosine_similarity([query_emb], docs_emb)[0]

index, score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)[0]

print(document[index])
print(score)