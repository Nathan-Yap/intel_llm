from fastapi import FastAPI
from langchain_community.llms import HuggingFaceHub
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from IPython.display import display
from PIL import Image
from pydantic import BaseModel
import base64
import io
from optimum.intel import OVModelForCausalLM

DEVICE = "cpu"
DTYPE = torch.float32 if DEVICE == "cpu" else torch.float16 # CPU doesn't support float16
MD_REVISION = "2024-05-20"

tokenizer = AutoTokenizer.from_pretrained("vikhyatk/moondream2", revision=MD_REVISION)
# tokenizer = AutoTokenizer.from_pretrained("nyap/cosmo-demo")
moondream_model = OVModelForCausalLM.from_pretrained(
    # "vikhyatk/moondream2", revision=MD_REVISION, trust_remote_code=True,
    "nyap/cosmo-demo", trust_remote_code=True,
    attn_implementation= None,
    torch_dtype=DTYPE, device_map={"": DEVICE}
)

from IPython.display import display
from PIL import Image

sample = Image.open("2banana.jpg")
display(sample)

# for qa in sample['qa']:
question = ""
print('Question:', question)
# print('Ground Truth:', qa['answer'])
print('Moondream:', moondream.answer_question(
    moondream.encode_image(sample),
    question,
    tokenizer=tokenizer,
))