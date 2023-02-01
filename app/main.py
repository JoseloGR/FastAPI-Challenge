from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import product, order

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router, tags=['Products'], prefix='/api/products')
app.include_router(order.router, tags=['Orders'], prefix='/api/orders')

@app.get("/api/healthcheck", tags=['Health'])
def health():
    return {"message": "tudo muito bem"}

