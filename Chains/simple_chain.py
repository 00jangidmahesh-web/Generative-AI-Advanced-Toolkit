from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI()

prompt = PromptTemplate(
    template = 'Generate 5 fun facts about {topic}',
    input_variables= ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'cats'})

print(result)

# Visulaize The Chain

chain.get_graph().print_ascii()