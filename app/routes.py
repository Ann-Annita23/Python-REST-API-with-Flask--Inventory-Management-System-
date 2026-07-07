from flask import Blueprint,jsonify,request
from app.models import inventory
inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory",methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@inventory_bp.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.get_json()

    if inventory:
        new_id = max(item["id"] for item in inventory) + 1
    else:
        new_id = 1

    new_item = {
        "id": new_id,
        "product_name":data["product_name"],
        "price":data["price"],
        "stock":data["stock"]
    }
    inventory.append(new_item)
    print("Current inventory", inventory)
    return jsonify(new_item), 201 # successfully created

@inventory_bp.route("/inventory/<int:id>", methods=["PATCH"])
def update_inventory(id):
    data = request.get_json()

    for item in inventory:
        if item["id"]==id:
            if "product_name" in data:
                item["product_name"] = data["product_name"]

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]
            return jsonify(item)  

    return jsonify({"message": "Item not found"}), 404

@inventory_bp.route("/inventory/<int:id>", methods=["DELETE"])
def delete_inventory(id):

    for item in inventory:
        if item["id"]==id:
            inventory.remove(item)
            return jsonify({"message":"Item deleted successfully"})

    return jsonify ({"message": "Item not found"}), 404

    

