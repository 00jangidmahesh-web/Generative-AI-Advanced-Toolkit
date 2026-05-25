
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# HuggingFaceEndPoint ---> This is the actual connection to the model to hugging face

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# You now have an LLM connection.... But it’s not chat-ready yet (becouse llms has no memory and no countinues Q/A capability)

model = ChatHuggingFace(llm=llm)
# Wraps your selected model into a chat-friendly format

result = model.invoke("What is the capital of India")

print(result.content)
