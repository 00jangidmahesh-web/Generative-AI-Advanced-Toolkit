from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system', 'you are a professional {profession}'),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human', 'Explain in simple terms about {topic}')
])

chat_history = []

# now load the previus chat history and append all messages in new list, jo as input jayegi
with open('chat_history.txt') as f:
    chat_history.extend(f.read())

prompt = chat_template.invoke(
    {
    'topic':'Attention Is all You Need',
    'chat_history':chat_history
    }
)

result = model.invoke(prompt)
print(result.content)