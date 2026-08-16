import uuid

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def request_id_middleware(
    request: Request,
    call_next
):

    request_id = str(uuid.uuid4())

    print(f"Request started: {request_id}")

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    print(f"Request completed: {request_id}")

    return response

@app.get("/students")
def get_students():
    return {
        "students": ["Noman", "Ali"]
    }