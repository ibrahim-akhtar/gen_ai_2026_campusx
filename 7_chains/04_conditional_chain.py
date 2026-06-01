from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# for parallel + branch(conditional) chains
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
# RunnableLambda - changes lambda func into runnable lambda

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

# prompt1 = PromptTemplate(
#     template='Classify the sentiment of the following feedback text into positive or negative: \n{feedback}',
#     input_variables=['feedback']
# )

# classifier_chain = prompt1 | model | parser
# modified below

# print(classifier_chain.invoke({'feedback':'This is a terrible smartphone'}))

# now we have to make sure that the output is consistent by being either positive or negative
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative: \n{feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback':'This is a terrible smartphone'}).sentiment

# print(result)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback\n{feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback\n{feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    # (condition1, chain1),
    # (condition2, chain2),
    # default chain

    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find any sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a terrible smartphone'})
print(result)

chain.get_graph().print_ascii()