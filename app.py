from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Supermarket Inventory API")

# Initializing Data as Tuples
products = ("Milk", "Eggs", "Bread", "Butter", "Cheese")
prices = (2.5, 3.0, 1.5, 4.0, 5.0)
stock = (10, 20, 15, 8, 5)


# Request schemas using Pydantic
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


class PriceUpdate(BaseModel):
    new_price: float


class StockUpdate(BaseModel):
    quantity: int


# ==========================================
# API Endpoints
# ==========================================


@app.get("/")
def root():
    return {"message": "Welcome to Supermarket Inventory API!"}


@app.get("/products")
def get_all_products():
    """1. Get all products with prices and stock levels"""
    inventory = []
    for i in range(len(products)):
        inventory.append(
            {
                "product": products[i],
                "price": prices[i],
                "stock": stock[i],
            }
        )
    return {"inventory": inventory}


@app.get("/products/{product_name}")
def get_product(product_name: str):
    """2. Search/Get details of a specific product"""
    if product_name in products:
        index = products.index(product_name)
        return {
            "product": products[index],
            "price": prices[index],
            "stock": stock[index],
        }
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def add_product(item: ProductCreate):
    """3. Add a new product to inventory"""
    global products, prices, stock

    if item.name in products:
        raise HTTPException(
            status_code=400, detail="Product already exists"
        )

    # Convert tuples to lists, append, and convert back to tuples
    products_list = list(products)
    prices_list = list(prices)
    stock_list = list(stock)

    products_list.append(item.name)
    prices_list.append(item.price)
    stock_list.append(item.stock)

    products = tuple(products_list)
    prices = tuple(prices_list)
    stock = tuple(stock_list)

    return {
        "message": f"Product '{item.name}' added successfully",
        "product": item.name,
        "price": item.price,
        "stock": item.stock,
    }


@app.put("/products/{product_name}/price")
def update_product_price(product_name: str, payload: PriceUpdate):
    """4. Update the price of a product"""
    global prices

    if product_name not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    index = products.index(product_name)
    prices_list = list(prices)
    prices_list[index] = payload.new_price
    prices = tuple(prices_list)

    return {
        "message": f"Updated {product_name} price to ${payload.new_price}",
        "product": product_name,
        "new_price": payload.new_price,
    }


@app.put("/products/{product_name}/stock")
def update_product_stock(product_name: str, payload: StockUpdate):
    """5. Update stock level (add or subtract stock)"""
    global stock

    if product_name not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    index = products.index(product_name)
    stock_list = list(stock)
    stock_list[index] += payload.quantity
    stock = tuple(stock_list)

    return {
        "message": f"Updated {product_name} stock to {stock[index]}",
        "product": product_name,
        "current_stock": stock[index],
    }


@app.delete("/products/{product_name}")
def delete_product(product_name: str):
    """6. Delete a product from inventory"""
    global products, prices, stock

    if product_name not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    index = products.index(product_name)

    products_list = list(products)
    prices_list = list(prices)
    stock_list = list(stock)

    products_list.pop(index)
    prices_list.pop(index)
    stock_list.pop(index)

    products = tuple(products_list)
    prices = tuple(prices_list)
    stock = tuple(stock_list)

    return {"message": f"Product '{product_name}' deleted successfully"}