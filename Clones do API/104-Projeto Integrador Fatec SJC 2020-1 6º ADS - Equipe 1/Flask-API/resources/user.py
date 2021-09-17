from  flask import Response, request
from database.model import User
from flask_restful import Resource

class UsersApi(Resource):
    #Get all users
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)
    #Register an user
    def post(self):
        body = request.get_json()
        user = User(**body).save()
        id = user.id
        return {'id': str(id)}, 200

class UserApi(Resource):
    #Tries to get an specific user by id
    def get(self, id):
        try:
            user = User.objects.get(id=id).to_json()
            return Response(user, mimetype="application/json", status=200)
        except:
            return Response("User not Found", status=500)
    #Update selected user
    def put(self, id):
        try:
            body = request.get_json()
            User.objects.get(id=id).update(**body)
            return '', 200
        except:
            return Response("User not Found", status=500)
    #Deletes selected user
    def delete(self, id):
        try:
            User.objects.get(id=id).delete()
            return 'User Removed', 200
        except:
            return Response("User not Found", status=500)