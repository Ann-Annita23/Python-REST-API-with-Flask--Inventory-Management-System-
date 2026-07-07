# Inventory Management System

## Overview

The Inventory Management System is a Python Flask REST API project that allows users to manage products through a Command Line Interface (CLI). Users can add, view, update, and delete inventory items. The application also integrates with the OpenFoodFacts API, allowing users to search for products by barcode and optionally add them to their inventory.

---

## Features

- View all inventory items
- Add a new product
- Update an existing product
- Delete a product
- Search for products using the OpenFoodFacts API
- Add products from OpenFoodFacts directly into the inventory
- Simple command-line interface
- REST API built with Flask

---

## Technologies Used

- Python 3
- Flask
- Requests
- REST API
- JSON
- Pytest (Testing)

---

## Project Structure

```
Week 2 Summative Lab/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
│
├── client/
│   └── cli.py
|   └── OpenFoodFacts.py
|
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

### Clone the repository

```bash
git clone https://github.com/Ann-Annita23/Python-REST-API-with-Flask--Inventory-Management-System-.git
```

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the virtual environment

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install flask requests pytest
```

---

## Running the Application

### Start the Flask server

```bash
python3 run.py
```

The server will run on

```
http://127.0.0.1:5000
```

### Start the CLI

Open another terminal.

Activate the virtual environment again, then run:

```bash
python3 client/cli.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /inventory | View all products |
| POST | /inventory | Add a new product |
| PATCH | /inventory/<id> | Update a product |
| DELETE | /inventory/<id> | Delete a product |

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

The application allows users to search products using a barcode.

Example barcode:

```
3017620422003
```

If a product is found, the application displays its details and gives the user the option to add it to the inventory.

---

## Running Tests

Run all tests using:

```bash
pytest
```

Or run a specific test file:

```bash
pytest tests/test_routes.py
```