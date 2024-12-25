from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    '''
    Testing base call
    '''
    return {"message": "Hello"}
