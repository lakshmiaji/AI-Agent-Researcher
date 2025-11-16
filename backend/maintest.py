# # Step1: Setup FastAPI backend
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()

# # Step2: Receive and validate request from Frontend
# class Query(BaseModel):
#     message: str

# @app.post("/ask")
# async def ask(query: Query):
#     response = "This is from backend"
#     return response

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload = True)