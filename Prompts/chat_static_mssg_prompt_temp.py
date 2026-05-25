from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

# chat_template = ChatPromptTemplate(
#     template='Tell me about {topic}, in detail including all formulas and codes',
#     input_variables=['topic']
# )
#    --------->   UPAR VALA CODE NOT WORK ----> IN CHAT MASSEGES

chat_template = ChatPromptTemplate([
    ('system', 'you are a professional {profession}'),
    ('human', 'Explain in simple terms about {topic}')
])

prompt = chat_template.invoke(
    {
    'topic':'Attention Is all You Need'
    }
)

result = model.invoke(prompt)
print(result.content)