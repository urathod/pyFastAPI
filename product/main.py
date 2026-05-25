from fastapi import FastAPI, Depends, status, Response, HTTPException
from product.routers import seller
from .schemas import DisplayProduct, DisplaySeller, Product, Seller
from . import models
from .database import engine, SessionLocal, Base
from .database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .routers import product, seller, login

app = FastAPI(
    title="Product API",
    description="API for managing products and sellers",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Uttam Rathod",
        "email": "uttamrathod@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    #docs_url="/documentation",
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


models.Base.metadata.create_all(bind=engine)
