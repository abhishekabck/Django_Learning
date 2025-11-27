from django.db.models import Subquery, OuterRef
from .models import Product
import requests

def generate(records):
    url = f"https://dummyjson.com/products?limit={records}"
    response = requests.get(url)
    data = response.json()

    products = list()
    for product_data in data['products']:
        try:
            product = Product(
                title = product_data['title'],
                description = product_data['description'],
                category = product_data['category'],
                price = product_data['price'],
                brand = product_data.get('brand', 'Unknown'),
                sku = product_data['sku'],
                thumbnail = product_data['thumbnail'],
            )
            product.save()
        except Exception as e:
            print(e)

