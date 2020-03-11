from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

# Resource is a class which allows GET POST UPDATE....)
class Student(Resource):
    # define the method that the resoure is going to get
    def get(self,name):
        return {"student": name}

# api works with resources (likely DB tables or class)
api.add_resource(Student, "/student/<string:name>") # http://127.0.0.1:5000/student/nick


app.run(port=5000)