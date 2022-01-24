import json

def load_products():
    with open("products.json") as f:
        return json.load(f)

def save_products():
    with open("products.json","w") as f:
        return json.dump(products,f)


products = load_products()