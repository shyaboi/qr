from flask import Flask
from flask_restful import Resource, Api
from routing import Chat
# from flask_cors import CORS

app = Flask(__name__)

# CORS(app)


api = Api(app)


api.add_resource(Chat, '/hB/<string:jwt>')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=False, threaded=True)