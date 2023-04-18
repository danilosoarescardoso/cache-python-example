from flask import Flask, jsonify
from flask_caching import Cache
import redis, time

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379'})

# fake products
products = [
    {
        'id': 1,
        'name': 'Product A',
        'description': 'This is product A with great features.',
        'price': 10.0
    },
    {
        'id': 2,
        'name': 'Product B',
        'description': 'This is product B with amazing capabilities.',
        'price': 20.0
    },
    {
        'id': 3,
        'name': 'Product C',
        'description': 'This is product C, the ultimate choice.',
        'price': 30.0
    },
    {
        'id': 4,
        'name': 'Product D',
        'description': 'This is product D, the most innovative product.',
        'price': 40.0
    }
]

# find product by id
def find_product(id):
    
    # Adding a simple delay to simulate an access to a database
    time.sleep(5)
    
    for product in products:
        if product['id'] == id:
            return product
    return None

# List all products
def find_products():
    time.sleep(2)

    return products

# Return all products
@app.route('/products')
@cache.cached(timeout=60)  # 60 seconds of cache
def get_products():
    return jsonify(find_products())

# Return a product by id
@app.route('/products/<int:id>')
@cache.cached(timeout=10)  # 10 seconds of cache
def get_product(id):
    return jsonify(find_product(id))

if __name__ == '__main__':
    app.run(debug=True)



