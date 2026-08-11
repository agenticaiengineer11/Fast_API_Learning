from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


def generete_data():
    yield "Hello\n"
    time.sleep(2)
    yield "this is\n"
    time.sleep(3)
    yield "streaming data\n"
    time.sleep(3)
@app.get("/stream")
def streaming_data():
    return StreamingResponse(
        generete_data(),
        media_type="text/plain"
    )
