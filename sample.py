from fastapi import FastAPI
application =FastAPI()

@application.get("/")
def home():
    return {"message":"this is home page "}
    
@application.get("/contact")
def contact():
    return {"message":"You can connect me anytime"}
