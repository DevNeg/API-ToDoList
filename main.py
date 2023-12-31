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

task = {
    'name':'Wash Dieshes','level':1,'situation':False,'limit':'12-12-2023'
}
tasks_list.append(task)
@app.post('/task_register')
def register(task:ToDo):
    try:
        tasks_list.append(task)
        return{'status':'The task now exist in your task data'}
    except:
        return{'status':'error'}

@app.post('/list_tasks')
def list_tasks(option: int = 1 ):
    try:
        if(option == 1):
            return tasks_list
        elif(option == 2):#just list the tasks already maded
            return list(filter(lambda x:x.situation == True, tasks_list))
        elif(option == 3):
            return list(filter(lambda x:x.situation == False, tasks_list))
    except:
        return{'status':'The option typed does not exist'}
    
@app.post('/list_one')
def list_one(id: int):
    try:
        return tasks_list[id]
    except:
        return{'status':'The id does not exist, please repeat'}

@app.post('/alter_task')
def alter(id:int):
    try:
        tasks_list[id].situation = not tasks_list[id].situation
        return {'status':f'The task situation is {tasks_list[id].situation}'}
    except:
        return{'status':'The id does not exist, please repeat'}



