import pytest
from app import create_app
from app.models import inventory

# HAPPY CODE
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

## TEST 1 => GET INVENTORY
def test_get_inventory(client):
    ## asks for inventory
    response = client.get("/inventory")
    ## If flask returned a status code thus checks if it's -> successful 
    assert response.status_code == 200

## TEST 2 => POST INVENTORY
def test_add_product(client):
    inventory.clear()

    response = client.post(
        "/inventory",
        json = {
            "product_name": "Milk",
            "": 50,
            "": 20,
        }
    )  
    assert response.status_code == 201
    data = response.get_json()
    assert data["product_name"]== "Milk" 

## TEST 3 => PATCH
def test_update_product(client):
    inventory.clear()
    inventory.append({
        "id": 1,
        "product_name": "Milk",
        "price": 50,
        "stock": 20
    })
    response = client.patch(
        "/inventory/1"
        json={
            "price":70
        }
    )     
    assert response.status_code == 200
    data = response.get_json()
    assert data["price"] == 70

def test_delete_product(client):
    inventory.clear()
    inventory.append({
        "id": 1,
        "product_name": "Milk",
        "price": 50,
        "stock": 20
    })
    response = client.delete("/inventory/1")
    assert response.status_code == 200
    assert len(inventory) == 0


