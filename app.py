from flask import Flask, render_template

app = Flask(__name__)


products = [
    {
        "id": 1,
        "name": "Wireless Noise-Cancelling Headphones",
        "category": "Audio",
        "price": 2499,
        "old_price": 2999,
        "tag": "FEATURED",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700"
    },
    {
        "id": 2,
        "name": "Smart Watch Series 5",
        "category": "Wearables",
        "price": 3299,
        "old_price": None,
        "tag": "NEW",
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=700"
    },
    {
        "id": 3,
        "name": "Fitness Tracker Band",
        "category": "Wearables",
        "price": 699,
        "old_price": 899,
        "tag": "SALE",
        "image": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=700"
    },
    {
        "id": 4,
        "name": "Ultrabook Laptop Pro",
        "category": "Computing",
        "price": 18999,
        "old_price": 19999,
        "tag": "POPULAR",
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
