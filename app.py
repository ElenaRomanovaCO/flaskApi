from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class TestFunc(Resource):
    def __init__(self):
        self.i = 0

    def get(self):
        self.i += 1
        return {
            'id': self.i
        }

api.add_resource(TestFunc, '/')

if __name__ == '__main__':
    app.run(debug=True)