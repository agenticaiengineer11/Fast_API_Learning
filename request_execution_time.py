print("======================Request Execution Time Middleware====================")

from fastapi import FastAPI,Request

import time

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("Request Recieved,",request)

    start_time = time.perf_counter()

    response = await call_next(request)
    response.headers["X-App-Version"] = "2.0"
    process_time = time.perf_counter() - start_time

    print(f"Response tooks {process_time:.4f} seconds")

    return response

@app.get("/students")
def get_student():
    return{
        "students":["Noman","Ali"] 
    }
