from fastapi import FastAPI
from models.dataWindow import Item
import models.dataWindow as m

app = FastAPI()

CONFIG = {
    'test': '/mt5/XAU_H1/test'
}

@app.get("/")
def read_root():
    return {"message": "Welcome to your local FastAPI server!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/mt5/XAU_H1/{name}")
def getXAUDATA(name: str):
    if not name:
        name = 'test_name'
    return {
        'key': "test",
        "value": name
    }

@app.post(CONFIG['test'])
def postTestData(msg: m.TestRequest):
    print('msg = ', msg)
    return {
        'code': 201,
        'message': 'success'
    }

@app.post('/mt5/XAU_H1')
def postXAUData(item: Item):
    if not item:
        print("no request body")
    
    print('item = ', item)
    return {
        'code': 201,
        'message': 'success'
    }

