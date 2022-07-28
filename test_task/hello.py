from typing import Dict, Union
from urllib import response
from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random
import uvicorn

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"

f = open('stat.txt', 'w', encoding='utf-8')
f.write(str(0))
f.close()    


@app.post('/model')
async def model(model:dict):    
    content = model
    if content['method'] == 'upper':
        y = content['text'].upper()
    elif content['method'] == 'lower':
        y = content['text'].lower()
    elif content['method'] == 'swapcase':
        y = content['text'].swapcase()   

    f = open('stat.txt', 'r', encoding='utf-8')
    stat  = int(f.readlines()[0])    
    f.close()
    stat += 1
    f = open('stat.txt', 'w', encoding='utf-8')
    f.write(str(stat))
    f.close()

    return str(y)

@app.get('/stat', response_class=PlainTextResponse)
async def stat():
    with open('stat.txt', 'r', encoding='utf-8') as f:
        return f.readlines()[0]        
   
