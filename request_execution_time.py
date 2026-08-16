from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware("http")
async def admin_check(request: Request, call_next):

    if request.url.path.startswith("/admin"):

        token = request.headers.get("X-Admin-Token")

        if token != "secret123":
            return JSONResponse(
                status_code=403,
                content={
                    "detail": "Admin access denied"
                }
            )

    response = await call_next(request)

    return response

@app.get("/admin/dashboard")
def admin_dashboard():
    return {
        "message": "Welcome Admin"
    }