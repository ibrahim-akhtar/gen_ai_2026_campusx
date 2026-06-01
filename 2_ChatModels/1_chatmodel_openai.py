from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4')

# parameters

# temperature - parameter that controls the randomness of lang models o/p.
#               it ffects how creative or deterministic the responses are.
# range from 0-2
# 0-0.3 - lower value - more deterministic & predictable answer
# 1.5+ - higher value - more random, creative & diverse response

# max_completion_tokens - parameter to restict the no of words/tokens the response should have

# chat_model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=10)

result = chat_model.invoke("What is the capital of India?")

print(result) # this will have a lot of metadata
print("-------------------")
print(result.content) # for the exact answer