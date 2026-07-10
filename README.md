# Inventory Management System

## Overview

The Inventory Management System is a Python Flask REST API project that enables users to manage products through a Command Line Interface (CLI). The application supports CRUD (Create, Read, Update, Delete) operations and integrates with the OpenFoodFacts API, allowing users to search for products by barcode or product name and optionally add them to their inventory.

---

## Features

- View all inventory items
- Add new products to the inventory
- Update existing products
- Delete products from the inventory
- Search products by barcode using the OpenFoodFacts API
- Search products by product name using the OpenFoodFacts API
- Add products retrieved from OpenFoodFacts directly into the inventory
- Command Line Interface (CLI) for interacting with the REST API
- Flask REST API supporting CRUD operations
- Unit testing using Pytest

---

## Technologies Used

- Python 3
- Flask
- Requests
- REST API
- JSON
- Pytest

---

## Project Structure

```text
Python-REST-API-with-Flask--Inventory-Management-System-/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
│
├── client/
│   ├── cli.py
│   └── OpenFoodFacts.py
│
├── tests/
│   └── test_routes.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ann-Annita23/Python-REST-API-with-Flask--Inventory-Management-System-.git
```

### 2. Navigate into the project directory

```bash
cd Python-REST-API-with-Flask--Inventory-Management-System-
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

#### Linux/macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Terminal 1: Start the Flask Server

```bash
python3 run.py
```

The server will start on:

```
http://127.0.0.1:5000
```

### Terminal 2: Start the Command Line Interface

Open a new terminal, activate the virtual environment, then run:

```bash
source venv/bin/activate
python3 client/cli.py
```

---

## CLI Menu

```
====== INVENTORY MANAGEMENT ======

1. View Inventory
2. Add Product
3. Update Product
4. Delete Product
5. Find Product on OpenFoodFacts
6. Exit
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/inventory` | Retrieve all inventory items |
| POST | `/inventory` | Add a new product |
| PATCH | `/inventory/<id>` | Update an existing product |
| DELETE | `/inventory/<id>` | Delete a product |

---

## Example Inventory Item

```json
{
    "id": 1,
    "product_name": "milk",
    "price": 50.0,
    "stock": 20
}
```

---

## OpenFoodFacts Integration

The application integrates with the OpenFoodFacts API, allowing users to:

- Search for products using a barcode
- Search for products by product name
- View product information such as:
  - Product name
  - Brand
  - Ingredients
- Add selected products directly into the inventory

### Example Barcode

```
3017620422003
```

### Example Product Name

```
Nutella
```

---

## Running Tests

Run all tests using:

```bash
python3 -m pytest
```

Run a specific test file:

```bash
python3 -m pytest tests/test_routes.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---