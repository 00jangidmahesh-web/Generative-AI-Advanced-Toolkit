'''       text
           │
     ┌─────┴─────┐
     │           │
   notes        quiz
     │           │
     └─────┬─────┘
           │
        merge
           │
        result
'''


from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name='claude-3')

parser = StrOutputParser()

text_gen = PromptTemplate(
    template='Generate a detailed report on the following topic \n {topic}',
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

chain = text_gen | model1 | parser

text = chain.invoke({'topic': 'black holes'})

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain


result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()
