from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# generator = pipeline('text-generation', model='gpt2', framework='pt')
generator = pipeline("text2text-generation", model="t5-base")
# Explicitly load model and tokenizer
# model = GPT2LMHeadModel.from_pretrained("gpt2")
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# generator = pipeline("text-generation", model=model, tokenizer=tokenizer, framework="pt")

app = FastAPI()


class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")


@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
