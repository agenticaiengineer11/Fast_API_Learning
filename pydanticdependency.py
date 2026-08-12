from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class ProductFilters(BaseModel):
    category: Optional[str] = None
    page: int = 1
    limit: int = 10


def get_product_filters(
    category: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return ProductFilters(
        category=category,
        page=page,
        limit=limit
    )


@app.get("/products")
def get_products(
    filters: ProductFilters = Depends(get_product_filters)
):
    return {
        "products": ["Mobile", "iPad"],
        "filters": filters
    }


@app.get("/featured-products")
def get_featured_products(
    filters: ProductFilters = Depends(get_product_filters)
):
    return {
        "featured_products": ["iPhone", "iPad2"],
        "filters": filters
    }