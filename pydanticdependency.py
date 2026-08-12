print("======================Pydantic&Dependency=====================")

from fastapi import FastAPI,Depends,Query
from pydantic import BaseModel

app = FastAPI()

class common_filters(BaseModel):
    search: str | None =None
    page: int = 1
    limit: int = 10

def get_filters(
        search: str | None = None,
        page: int = Query(1,ge=1),
        limit :int = Query(10,ge=1,le=100)
):
    return common_filters(
        search=search,
        page=page,
        limit=limit
    )
@app.get("/products")
def get_products(
    filters:common_filters = Depends(get_filters)
):
    return{
        "products": ["Laptop","charger"],
        "filter": filters
    }
@app.get("/orders")
def get_orders(
    filters:common_filters = Depends(get_filters)
):
    return{
        "orders": ["order1","order2"],
        "filters": filters
    }
