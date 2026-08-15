from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def my_middleware(request: Request, call_next):

    print("Request received:", request.method, request.url.path)

    response = await call_next(request)

    print("Response generated")

    return response


@app.get("/students")
def get_students():
    print("Student endpoint executed")

    return {
        "students": ["Noman", "Ali"]
    }