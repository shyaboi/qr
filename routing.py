from flask_restful import Resource, Api, reqparse

class Chat(Resource):
    def get(self, jwt):
        parser = reqparse.RequestParser()
        chat = parser.add_argument('jwt',jwt)
        args = parser.parse_args()
        print(args)
        return args