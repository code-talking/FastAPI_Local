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

@app.get("/mt5/{symbol}/{data_frame}")
def read_params(symbol: str = 'symbol', data_frame: str = None, serverTime: str = None):
    print(f"Received parameters - symbol: {symbol}, data_frame: {data_frame}, serverTime: {serverTime}")
    return {
        "symbol": symbol,
        "serverTime": serverTime,
        "data_frame": data_frame
    }