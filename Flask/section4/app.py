from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

# Resource is a class which allows GET POST UPDATE....)
class Item(Resource):
    # define the method that the resoure is going to get
    def get(self,name):
        for item in items:
            if item["name"] == name:
                return item #return 200 as status cod
        return {"item":None}, 404

    def post(self,name):
        item = {"name": name, "price": 66.66}
        items.append(item)
        return item, 201 # return 201 for creating successfully

# api works with resources (likely DB tables or class)
api.add_resource(Item, "/item/<string:name>") # http://127.0.0.1:5000/item/<name>


app.run(port=5000)