import requests
def menu():
    print("\n====== INVENTORY MANAGEMENT ======")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Find Product on OpenFoodFacts")
    print("6. Exit")

def main():
    while True:
        menu()    
        try:
            choice = input("Choose an Option: ")
               ## 1. View Inventory     
            if choice == "1":
                response = requests.get("http://127.0.0.1:5000/inventory")
                items = response.json()
                print(items)
                if not items:
                    print("\n Inventory is empty\n")
                else:
                    print("\n ====== INVENTORY ======\n")
                    for item in items:
                        print(f"ID: {item['id']}")  
                        print(f"Product: {item['product_name']}") 
                        print(f"Price: {item['price']}") 
                        print(f"stock: {item['stock']}") 
                        print("-----------------------------------") 
                        
                ## Add Product
            elif choice == "2":
                product_name = input("Enter product name: ").strip().lower()
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))

                new_item = {
                    "product_name": product_name,
                    "price": price,
                    "stock": stock
                }
                response = requests.post(
                    "http://127.0.0.1:5000/inventory",
                    json=new_item
                )
                print(response.json())

                 ## Update product   
            elif choice == "3":
                response = requests.get("http://127.0.0.1:5000/inventory")
                items = response.json()
                if not items:
                    print("Inventory is empty.")
                else:
                    print("\n====== CURRENT INVENTORY ======\n") 
                    for item in items:
                        print(f"ID: {item['id']}")
                        print(f"Product: {item['product_name']}")
                        print(f"Price: {item['price']}")
                        print(f"Stock: {item['stock']}")
                        print("-------------------------------------")
                    product_id = int(input("Enter the ID of the product to update: ")) 
                    product_name = input("Enter new product name: ").strip().lower()
                    price = float(input("Enter new price: "))
                    stock = int(input("Enter new stock quantity: "))

                    update_item = {
                        "product_name": product_name,
                        "price": price,
                        "stock": stock
                    }  

                    response = requests.patch(
                        f"http://127.0.0.1:5000/inventory/{product_id}",
                        json = update_item
                    ) 
                    print(response.json())

                ## Delete Product
            elif choice == "4":
                response = requests.get("http://127.0.0.1:5000/inventory")
                items = response.json()

                if not items:
                    print("Inventory is empty.")
                else:
                    print("\n====== CURRENT INVENTORY ======\n")
                    for item in items:
                        print(f"ID: {item['id']}") 
                        print(f"Product: {item['product_name']}") 
                        print(f"Price: {item['price']}") 
                        print(f"Stock: {item['stock']}") 
                        print("------------------------------------")

                    product_id = int(input("Enter the ID of the product to delete: "))
                    response = requests.delete (
                        f"http://127.0.0.1:5000/inventory/{product_id}"
                    ) 
                    print(response.json())  
                
                ## External API
            elif choice == "5":
                try:
                    print("\n======OPEN FOOD FACTS ======")
                    print("1. Search by Barcode")
                    print("2. Search by Product Name")

                    search_choice = input("Choose an Option: ")
                    if search_choice == "1":
                        barcode = input("Choose an Barcode: ")
                # --------------------------Barcode Search-----------------------        

                        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
                        headers = {
                            "User-Agent": "FoodApp/1.0 "
                        }
                        response = requests.get(url, headers=headers)
                        data = response.json()
                        if data["status"] == 1:

                            product = data["product"]

                            print("\n====== PRODUCT FOUND ======")
                            print(f"Name: {product.get('product_name', 'N/A')}")
                            print(f"Brand: {product.get('brands','N/A')}")
                            print(f"Ingredients: {product.get('ingredients_text', 'N/A')}")
                            
                            add = input("\nAdd this product to inventory?(y/n): ")
                            
                            if add.lower() =="y":
                                price = float(input("Enter price: "))
                                stock = int(input("Enter stock quantity: "))

                                new_item = {
                                    "product_name": product.get("product_name", "Unknown Product"),
                                    "price": price,
                                    "stock": stock
                                }

                                response = requests.post(
                                    "http://127.0.0.1:5000/inventory",
                                    json = new_item
                                )

                                print(response.json())
                            else:
                                print("Product not found.")
                    #------------------------ Name Search --------------------
                    elif search_choice == "2":
                        product_name = input("Enter product name: ")
                        
                        url =(
                            f"https://world.openfoodfacts.org/cgi/search.pl?"
                            f"search_terms={product_name}"
                            "&search_simple=1"
                            "&action=process"
                            "&json=1"
                        )
                        response = requests.get(url)
                        data = response.json()
                        if data["products"]:
                            product = data["products"][0]
                            print("\n====== PRODUCT FOUND ======")
                            print(f"Name: {product.get('product_name','N/A')}")
                            print(f"Brand: {product.get('brands', 'N/A')}")

                            add = input("\n Add this product to inventory? (y/n): ")
                            if add.lower() == "y":

                                price =float(input("Enter price: "))
                                stock = int(input("Enter stock quantity: "))

                                new_item ={
                                    "product_name": product.get("product_name", "Unknown Product"),
                                    "price": price,
                                    "stock": stock
                                }

                                response = requests.post(
                                    "http://127.0.0.1:5000/inventory",
                                    json = new_item
                                )
                                print(response.json())
                            else: 
                                print("Product wasnot added")
                        else:
                            print("No products found")
                except Exception as e:
                        print(e)                                
            ## Breakin Point
            elif choice == "6":
                print("Thank you for using Inventory Management System.")
                break
            else:
                print("Invalid option. Please choose between 1 and 6") 
        except Exception as e:
            print(f"An error has occurred: {e}")

if __name__ == "__main__":
    main()

              
                  
     


            



