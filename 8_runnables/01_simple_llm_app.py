# user -> topic
#  |
# prompt
#  |
# llm -> display

from langchain.llms import OpenAI           # not using ChatModel i.e. creating llm with the help of llm component
from langchain.prompts import PromptTemplate

# initialize the llm
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about the {topic}."
)

# define the input
topic = input("Enter a topic: ")

# format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

# call the llm directly
blog_title = llm.predict(formatted_prompt)

# print the output
print("Generated Blog Title:", blog_title)