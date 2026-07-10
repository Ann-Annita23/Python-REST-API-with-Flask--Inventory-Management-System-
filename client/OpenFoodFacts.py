import requests

class OpenFoodFacts():
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org/api/v0"
    
    def get_product(self,barcode):
        url = f"{self.base_url}/product/{barcode}.json"   
        response = requests.get(url)
        return response.json()


