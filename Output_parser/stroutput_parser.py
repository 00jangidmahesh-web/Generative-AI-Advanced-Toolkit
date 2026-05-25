from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

# topic: black hole, milte hi chain active
# template1 --> prompt ready karega jisme topic added hai
# model --> use prompt ko lega, result generate karega
# parser --> pure result me se content fetch karego jo next stage me required hai
# template2 --> use content ko lega or uske sath question attach karega.... give 5 line summary
# model --> again send new question to model


result = chain.invoke({'topic':'black hole'})

print(result)