from pydantic import BaseModel, ConfigDict
from typing import List, Optional

# Schemas de Produto
class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    store_id: int
    # Nova sintaxe V2
    model_config = ConfigDict(from_attributes=True)

# Schemas de Loja
class StoreBase(BaseModel):
    name: str
    category: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    is_active: bool
    products: List[Product] = []
    # Nova sintaxe V2
    model_config = ConfigDict(from_attributes=True)
