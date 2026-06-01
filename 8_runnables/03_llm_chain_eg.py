from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# load th llm
llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0.7)

# create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"], # defines what input is needed
    template="Suggest a catchy blog title about {topic}.
)

# crate an llm chain
chain = LLMChain(llm=llm, prompt=prompt)

# run the chain with a specific topic
topic = input("Enter a topic")
output = chain.run(topic)

print("Generated Blog Title:", output)