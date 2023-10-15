from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()
tasks_list = []
class ToDo(BaseModel):
    name:str
    level:int
    situation:bool
    limit:date

@app.post('/task_register')
def register(task:ToDo):
    try:
        tasks_list.append(task)
        return{'status':'success'}
    except:
        return{'status':'error'}

@app.post('/list_tasks')
def list_tasks(option: int = 0 ):
    try:
        if(option == 0):
            return tasks_list
        elif(option == 1):#just list the tasks already maded
            return list(filter(lambda x:x.situation == True, tasks_list))
        elif(option == 2):
            return list(filter(lambda x:x.situation == False, tasks_list))

    except:
        return{'status':'error'}

