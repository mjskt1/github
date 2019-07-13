from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}

api.add_resource(HelloWorldResource, '/')

# 此处启动对于1.0之后的Flask可有可无
if __name__ == '__main__':
    app.run(debug=True,host='192.168.196.130')