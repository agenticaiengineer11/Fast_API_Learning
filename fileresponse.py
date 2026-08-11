from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download")
def get():
    return FileResponse("requirements.txt")
