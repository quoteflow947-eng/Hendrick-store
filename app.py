
from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Studio Wireless Headphones",
        "category": "Audio",
        "price": 1299,
        "old_price": 1599,
        "tag": "BESTSELLER",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700"
    },
    {
        "id": 2,
        "name": "Smartphone Pro",
        "category": "Gadgets",
        "price": 8999,
        "old_price": None,
        "tag": "NEW ARRIVAL",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=700"
    },
    {
        "id": 3,
        "name": "Classic Smart Watch",
        "category": "Wearables",
        "price": 2199,
        "old_price": 2499,
        "tag": "POPULAR",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700"
    },
    {
        "id": 4,
        "name": "Ultra Slim Laptop",
        "category": "Computing",
        "price": 12499,
        "old_price": None,
        "tag": "PREMIUM",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=700"
    },
    {
        "id": 5,
        "name": "Portable Bluetooth Speaker",
        "category": "Audio",
        "price": 899,
        "old_price": 1099,
        "tag": "SALE",
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=700"
    },
    {
        "id": 6,
        "name": "Wireless Gaming Controller",
        "category": "Gadgets",
        "price": 1099,
        "old_price": None,
        "tag": "FEATURED",
        "image": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=700"
    },
    {
        "id": 7,
        "name": "Premium Digital Camera",
        "category": "Gadgets",
        "price": 7499,
        "old_price": 7999,
        "tag": "POPULAR",
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=700"
    },
    {
        "id": 8,
        "name": "Wireless Earbuds",
        "category": "Audio",
        "price": 799,
        "old_price": None,
        "tag": "NEW",
        "image": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=700"
    }
]


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/health")
def health():
    return {"status": "Hendrick Store is running"}


if __name__ == "__main__":
    app.run(debug=True)
