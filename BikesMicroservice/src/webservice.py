from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Bikes(Resource):
    def get(self):
        Items = '{ "vin":"AK123ZW", "brand":"Ducati", "Model":"Panigale"}'
        return {
            'statusCode': 200,
            'headers': {
                "x-custom-version" : "1.0"
            },
            'body': json.dumps(Items)
        }
    def put(self):
        vin = "AK123ZW"
        return {
            'statusCode': 201,
            'headers': {
                'headers': {
                "x-custom-version" : "1.0"
                },
            },
            'body': json.dumps({'msg': 'Bike created'+vin})
        }
    def post(self):
        vin = "AK123ZW"
        return {
            'statusCode': 200,
            'headers': {
                'headers': {
                "x-custom-version" : "2.1"
                },
            },
            'body': json.dumps({'msg': 'Bike updated '.join(vin)})
        }
    
api.add_resource(Bikes, '/bikes')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

