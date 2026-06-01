from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# import os
# os.environ['HP_HOME'] = 'D:/huggingface_cache'

# model used: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 
llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)


chatModel = ChatHuggingFace(llm=llm)

result = chatModel.invoke("What is the capital of India?")

print(result.content)