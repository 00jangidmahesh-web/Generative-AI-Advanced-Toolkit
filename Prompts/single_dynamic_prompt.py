from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template='Tell me about {topic}, in detail including all formulas and codes',
    input_variables=['topic']
)

prompt = template.invoke(
    {
    'topic':'Attention Is all You Need'
    }
)
result = model.invoke(prompt)
print(result.content)