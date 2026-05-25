from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated

# Annoted ---> used for telling AI more about what you want, like attaching example or discription etc

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):

    summary : Annotated[str, "summary of the review"]
    sentiment : str
    language : str
    stars : int

structured_model = model.with_structure_output(Review)

result = structured_model.invoke('''The product is great, 
                                 but the metrial you use is too low quality, 
                                 other brands offer better then it.''')

print(result)
