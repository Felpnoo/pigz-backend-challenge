from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

# 1. Configura Banco em Memória (SQLite)
# CheckSameThread=False é necessário apenas para SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas nesse banco vazio
Base.metadata.create_all(bind=engine)

# 2. Override da Dependência (Troca o banco real pelo de teste)
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# --- 3. OS TESTES REAIS ---

def test_create_store():
    # Tenta criar uma loja
    response = client.post(
        "/stores/",
        json={"name": "Hamburgueria Teste", "category": "Lanches"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Hamburgueria Teste"
    assert "id" in data

def test_read_stores():
    # Lista as lojas (deve ter a que criamos acima ou estar vazia se reiniciar)
    response = client.get("/stores/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product_for_store():
    # Primeiro cria a loja
    store_res = client.post(
        "/stores/",
        json={"name": "Pizzaria", "category": "Pizza"}
    )
    store_id = store_res.json()["id"]

    # Depois cria o produto nela
    response = client.post(
        f"/stores/{store_id}/products/",
        json={"name": "Pizza Gigante", "price": 59.90}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pizza Gigante"
    assert data["store_id"] == store_id

def test_create_product_invalid_store():
    # Tenta criar produto numa loja que não existe (ID 9999)
    response = client.post(
        "/stores/9999/products/",
        json={"name": "Erro", "price": 10.0}
    )
    assert response.status_code == 404
