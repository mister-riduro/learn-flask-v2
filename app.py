from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#initiate flask object
app = Flask(__name__)

#initiate Api object
api = Api(app)

#CORS
CORS(app)

users = {}

class UsersResource(Resource):
    def get(self):
        # response = {"message" : "success get all users"}
        return users

    def post(self):
        name = request.json["name"]
        age = request.json["age"]

        users["name"] = name
        users["age"] = age

        response = {"message" : "success create user"}
        return response

api.add_resource(UsersResource, "/users", methods=["GET", "POST"])

if __name__ == "__main__" :
    app.run(debug=True, port=2002)