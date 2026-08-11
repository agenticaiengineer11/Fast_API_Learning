from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def status():
    return PlainTextResponse(
        "Server is working successfully"
    )