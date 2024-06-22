from fastapi import FastAPI
from langchain_community.llms import HuggingFaceHub

app = FastAPI()

# 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
huggingfacehub_api_token = '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'

llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/falcon")
async def falcon(prompt: str):
    output = llm.invoke(prompt)
    return {"message": output}
