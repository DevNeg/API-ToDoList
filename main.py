from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI
tasks_list = []
class ToDo(BaseModel):
    name:str
    level:int
    did:bool
    limit:date

