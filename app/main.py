from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database

# Cria as tabelas no banco automaticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Pigz Challenge API")

# --- ROTAS DE LOJA ---
@app.post("/stores/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(database.get_db)):
    db_store = models.Store(name=store.name, category=store.category)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

@app.get("/stores/", response_model=List[schemas.Store])
def list_stores(db: Session = Depends(database.get_db)):
    return db.query(models.Store).all()

# --- ROTAS DE PRODUTO ---
@app.post("/stores/{store_id}/products/", response_model=schemas.Product)
def create_product(store_id: int, product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    # Verifica se a loja existe
    store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    
    db_product = models.Product(**product.model_dump(), store_id=store_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
