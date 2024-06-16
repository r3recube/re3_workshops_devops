from flask import Flask
from flask_restful import Resource, Api
from flask import request
import json

app = Flask(__name__)
api = Api(app)

class Cars(Resource):
    def get(self):
        Items = '{ "vin":"AK123ZW", "brand":"Ducati", "Model":"Panigale"}'
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())
        return {
            'statusCode': 200,
            'headers': {
                "x-custom-version" : "1.0"
            },
            'body': json.dumps(Items)
        }
    def put(self):
        vin = "AK123ZW"
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())
        return {
            'statusCode': 201,
            'headers': {
                'headers': {
                "x-custom-version" : "1.0"
                },
            },
            'body': json.dumps({'msg': 'Car created'+vin})
        }
    def post(self):
        vin = "AK123ZW"
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())
        return {
            'statusCode': 200,
            'headers': {
                'headers': {
                "x-custom-version" : "2.1"
                },
            },
            'body': json.dumps({'msg': 'Car updated '.join(vin)})
        }
    
api.add_resource(Cars, '/cars')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

