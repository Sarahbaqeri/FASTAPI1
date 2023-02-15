from fastapi import FastAPI
from todo import todo_router

app =FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message":"hello world"}

app.include_router(todo_router)