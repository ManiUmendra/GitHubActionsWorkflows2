from fastapi import FastAPI, Form, Body,Path,Query,UploadFile,File
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
async def root():
    return "hello"

@app.post('/')
async def my_post():
    return "Post"

# @app.put('/')
# async def my_get():
#     return "Put"

@app.get('/{item_id}')
async def get_item_id(item_id):
    if item_id=="1":
        return {"item_id":item_id}
    else:
        return "Null"

@app.get('/{item_id}/user/{user_id}')
async def get_values(item_id: int,user_id:int,val:str=''):
    return {'item_id':item_id,"value":val,'user_id':user_id}

class Item(BaseModel):
    name:str
    id:int
    salary:str

@app.post('/{items_d}/items')
async def record(items_d:int,item:Item):
    return item

@app.get('/login/{item_id}')
async def loginapi(*,item_id:int=Path(...,title="Enter Path"),q:str):
    return {'q':q}

@app.post('/login/form/')
async def login_form(username: str=Form(...),password: str=Form(...)):
    return {"username":username}

@app.get('/query/{a}')
async def query(q:list[str]=Query(...),a:str=Path(...)):
    return q

@app.post('/files/')
async def get_files(q:bytes):
    return q.filename

@app.post('/Uploadfiles/')
async def upload_file(q:UploadFile=File(...)):
    return q.filename

@app.post('/postman')
async def get_postman(a:int=0,b:int=0):
    return {a*b}
    