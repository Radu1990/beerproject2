from flask import Flask, request
from flask_restful import abort, Api, Resource
import requests

import beerproject.database_commands as bdc

app = Flask(__name__)
api = Api(app)


# this fn checks if id is already given
def abort_if_beer_doesnt_exist(beer_id, all_ids):
    beer_id_to_int = int(beer_id)
    if beer_id_to_int not in all_ids:
        abort(404, message="Beer %s doesn't exist yet in the table" % beer_id)


# Check or edit
# GETS a single beer item
class Editbeer(Resource):

    def get(self, beer_id):

        # checking if id is already in table
        connection = bdc.create_connection()
        all_ids = bdc.select_return_all_ids(connection)
        abort_if_beer_doesnt_exist(beer_id, all_ids)

        # displaying item if test is ok
        connection = bdc.create_connection()
        item = bdc.select_item(connection, beer_id)
        return item

    def delete(self, beer_id):

        # checking if id is already in table
        connection = bdc.create_connection()
        all_ids = bdc.select_return_all_ids(connection)
        abort_if_beer_doesnt_exist(beer_id, all_ids)

        # deleting item
        connection = bdc.create_connection()
        bdc.delete_item(connection, beer_id)
        return '', 204

    def put(self, beer_id):

        # checking if id is already in table
        connection = bdc.create_connection()
        all_ids = bdc.select_return_all_ids(connection)
        abort_if_beer_doesnt_exist(beer_id, all_ids)

        # updating item
        connection = bdc.create_connection()
        data = request.json
        bdc.update_item(connection, beer_id, data)
        return '', 201


# Add new beers
# shows a list of all beers, and lets you POST to add new beers
class Checkbeer(Resource):
    def get(self):
        connection = bdc.create_connection()
        data = bdc.select_return_all(connection)
        return data

    def post(self):

        connection = bdc.create_connection()
        data = request.json
        bdc.insert_new_beer(connection, data)
        return '', 201


## Actually setup the Api resource routing here
##
api.add_resource(Checkbeer, '/beercheck')
api.add_resource(Editbeer, '/beercheck/<beer_id>')


if __name__ == '__main__':
    app.run(debug=True)

# initialising the table with preset values
conn = bdc.create_connection()
bdc.table_init(conn)
conn.close()
#hjiasdijasd
