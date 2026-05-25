from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = 'Generate detailed report on {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = 'Give most important 5 points from \n {report}',
    input_variables= ['report']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)

# Visulaize The Chain

chain.get_graph().print_ascii()