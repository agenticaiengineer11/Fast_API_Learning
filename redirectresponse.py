from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/old")
def old_page():
    return RedirectResponse(url="/new")

@app.get("/new")
def new_page():
    return {
        "message": "You are now on the new page"
    }
@app.get("/google")
def google():
    return RedirectResponse(
        url="https://www.google.com"
    )