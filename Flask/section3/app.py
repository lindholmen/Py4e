from flask import Flask,jsonify, request, render_template

app = Flask(__name__)

# SERVER PERSPECTIVE:
# POST - RECEIVE DATA AND USE IT
# GET - SEND DATA
# PUT
# DELETE

# STATELESS

stores = [
    {
        "name": "LA shoes store",
        "items": [
            {
                "name":"Kobe 11 shoes",
                "price": 35.99
            },
            {
                "name":"James 10 shoes",
                "price": 11.99
            }
        ]
    },
    {
        "name": "DC jersey store",
        "items": [
            {
                "name":"Kobe 8",
                "price": 99.99
            },
            {
                "name":"Kobe 24",
                "price": 109.99
            }
        ]
    }
]


@app.route("/") # access to the end point, by default it is a GET request
def home():
    #return "hello world" # when requesting the home route, return the str as a response
    return render_template("index.html")

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    # Get the json data from request and convert it to a dictionary
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            # here store is a dict so directly jsonify it
            return jsonify(store)
    return jsonify({"message":"store not found"})

# GET /store
@app.route("/store")
def get_stores():
    # json can be a dictionary or list alike, but jsonify ask for a dictionary
    # in JS JSON is string '{"x":"y"}' and you must use apostrophe
    # 这里相当于把stores这个list 封装为一个dictionary
    return jsonify({"stores": stores})

# POST /store/<string:name>/item {name:  ,price: }
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        "name": request_data["name"],
        "price": request_data["price"]
    }
    for store in stores:
        if store["name"] == name:
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message":"store not found"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"]== name:
            return jsonify({"item":store["items"]})
    return jsonify({"message":"store not found"})




app.run(port=5000)

# find the process that takes the 5000 port
# sudo lsof -i :3000
# kill it
# kill -9 <PID>
