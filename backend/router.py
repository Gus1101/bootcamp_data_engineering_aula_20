### Arquivo responável pelas rotas de API

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductRead, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product_by_id,
    delete_product,
    update_product
)

router = APIRouter()

@router.get("/products/", response_model=List[ProductRead])
def read_all_products_route(db: Session = Depends(get_db)):
    """
    Rota para consulta dos produtos do banco de dados
    """
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductRead)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    Rota para consultar um produto do banco de dados
    """
    db_product = get_product_by_id(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não existe")
    return db_product

@router.post("/products/",response_model=ProductRead)
def create_a_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Rota para adicionar um produto ao banco de dados
    """
    return create_product(product=product, db=db)

@router.delete("/products/{product_id}", response_model=ProductRead)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Rota para deletar um produto do banco de dados
    """ 
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Produto não existe")
    return product_db

@router.put("/products/{product_id}", response_model=ProductRead)
def update_a_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """
    Rota para alterar informações de um produto no banco de dados
    """
    product_db = update_product(product_id=product_id, db=db, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, details="Produto não existe")
    return product_db

