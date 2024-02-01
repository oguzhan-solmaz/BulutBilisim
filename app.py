
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Player(Resource):
    def get(self):
       data = pd.read_csv('Player.csv')
       data = data.to_dict('records')
       return { 'data' : data}, 200

    def post(self):
        name = request.args['name']
        position = request.args['position']
        team = request.args['team']

        data = pd.read_csv('Player.csv')

        new_data = pd.DataFrame({
            'name': [name],
            'position': [position],
            'team': [team]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('Player.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

class Name(Resource):
    def get(self):
        data = pd.read_csv('Player.csv', usecols=[0])
        data = data.to_dict('records')
        return {'data': data}, 200

api.add_resource(Name, '/playername')
api.add_resource(Player, '/Player')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
