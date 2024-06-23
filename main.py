from fastapi import FastAPI
from langchain_community.llms import HuggingFaceHub
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from IPython.display import display
from PIL import Image
from pydantic import BaseModel
import base64
import io

app = FastAPI()

DEVICE = "cpu"
DTYPE = torch.float32 if DEVICE == "cpu" else torch.float16 # CPU doesn't support float16
MD_REVISION = "2024-05-20"

tokenizer = AutoTokenizer.from_pretrained("vikhyatk/moondream2", revision=MD_REVISION)
# tokenizer = AutoTokenizer.from_pretrained("nyap/cosmo-demo")
moondream_model = AutoModelForCausalLM.from_pretrained(
    # "vikhyatk/moondream2", revision=MD_REVISION, trust_remote_code=True,
    "nyap/cosmo-demo", trust_remote_code=True,
    attn_implementation= None,
    torch_dtype=DTYPE, device_map={"": DEVICE}
)

# # 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
# huggingfacehub_api_token = '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'

# llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

class Data(BaseModel):
    image: str

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
# @app.get("/falcon")
# async def falcon(prompt: str):
#     output = llm.invoke(prompt)
#     return {"message": output}

@app.post("/moondream")
async def moondream(data: Data):
    # Decode the base64 image data
    image_data = base64.b64decode(data.image)
    # Convert the binary data to a PIL image
    with open("test.jpg", 'wb') as f:
        f.write(image_data)
    pil_image = Image.open("test.jpg")
    
    # Perform any further processing on the PIL image here
    # For demonstration, let's just convert it to a grayscale image    
    # pil_image.save("test.jpg")
    # Optionally save or manipulate the processed image
    # processed_image.save("processed_image.jpg")  # Example of saving the processed image
            
    answer = moondream_model.answer_question(
        moondream_model.encode_image(pil_image),
        "",
        tokenizer=tokenizer,
    )    

    payload = []

    for item in answer.split(','):
        item.strip()
        count, produce = item.split()
        payload.append({"ingredient": produce.strip(), "count": count.strip()})
    # Return a response with a message or any processed data
    return {"data": payload}

