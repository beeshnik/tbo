from fastapi import FastAPI, UploadFile, File
from random import randint

app = FastAPI()

trash = {"glass": randint(0, 10), "wood": randint(0, 10), "metal": randint(0, 10), "plastic": randint(0, 10)}



@app.post("/")
async def root_post(file: UploadFile = File(...)):
    return {"file_name": file.filename}


@app.get("/")
async def root_get():
    return trash
