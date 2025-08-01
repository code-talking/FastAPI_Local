from pydantic import BaseModel

# class DataWindow():


class TestRequest(BaseModel):
  msg: str

class Item(BaseModel):
  time: str
  color: str
  price: str