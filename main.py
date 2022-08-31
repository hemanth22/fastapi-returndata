from typing import Optional
from fastapi import FastAPI
from enum import Enum

def goGo():
    print("Go is language used for designing cutting edge technology")

class Language(str, Enum):
    python = "python"
    java = "java"
    go = "go"
    dart = "dart"


app = FastAPI()

@app.get('/')
async def root():
    return {'message' : 'Hello World'}

@app.get("/lang/{lang}")
async def getlanguage(lang:Language):
    if(lang == Language.python):
        return {"message": "Python is wonderful language for machine learning"}
    elif(lang == Language.java):
        return {"message": "Java is wonderful language for web and desktop apps"}
    elif(lang == Language.go):
        return goGo()
    return {"message":"Dart is a relatively new language used for flutter apps"}
