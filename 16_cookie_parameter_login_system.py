from fastapi import FastAPI,Cookie,HTTPException,Response
from pydantic import BaseModel
from typing import Annotated
from uuid import uuid4

app=FastAPI()

#Database
users={"dassg360@gmail.com":{
    "password":"Gopal@123",
    "name":"Gopal"
}}

sessions={}
class Login(BaseModel):
    email:str
    password:str

@app.post("/login")
async def login_request(data:Login,response:Response):
    # storing the email in user and the user exist or not in users database
    user=users.get(data.email)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid email")
    if user["password"]!=data.password:
        raise HTTPException(status_code=401,detail="Invalid password")
    #creating session id with uuid4() and storing it in the sessions dictionary with user email
    session_id=str(uuid4())
    sessions[session_id]=data.email
    print(sessions)
    # store session id in the browser
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True    
    )
    return {"Message":"Login successfully"}

@app.get("/Dashboard")
async def dashboard(session_id:Annotated[str|None,Cookie()]=None):
    if not session_id:
        raise HTTPException(status_code=401,detail="Not login")
    email=sessions.get(session_id)
    if not email:
        raise HTTPException(status_code=401,detail="Invalid session")
    print(session_id)
    return {
        "message": "Welcome to dashboard",
        "email": email
    }