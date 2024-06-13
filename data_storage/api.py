"""This code uses `pymongo`, `json` to create, read, update, delete the json
data in a server.
"""
import pymongo
import json
from pymongo.errors import ConnectionFailure


def check_server_status(client):
    """
    Check if the mongod server is running in the background. Else
    raise an error and stop the program.
    """
    # Make sure the server is running. Else exit with a message
    try:
        client.admin.command('ismaster')
    except (ConnectionFailure) as exptn:
        print("Server not available.\nPlease run:\n `sudo systemctl start mongod`")
        raise SystemExit(0) from exptn


class MyData():
    """A class to save json data into a data base. This class provides with basic
    operations to operate on the data, such as: `create`, `get`, `update`,
    `delete`. This class is typically used as follows:


        data = MyData(database="db", collection="collection")

    The CRUD operations on the data can be executed using the follwing
    provided methods:

    1. insert: Insert json data into the database.

    2. insert_from_file: Insert json data into the database using a json file.

    3. get: Get data from the database using an id

    4. update: Update a data based on the id and updated json value.

    5. delete: Delete a value in the database from a given id.


    The MyData instance has the following attributes:
    - ``client``: A connection to the server

    - ``database``: The database in the mongod server

    - ``collection``: The collection in the database where the data is
      saved

    """
    def __init__(self, database, collection, json_data=None):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/",
                                          serverSelectionTimeoutMS=5)
        check_server_status(self.client)

        # create the databse and the collection
        self.database = self.client[database]
        self.collection = self.database[collection]

        # Before inserting the data (json), make sure it is a valid data
        if json_data is not None:
            try:
                self.insert(json_data)
            except:
                print("The Json data is not valid")

    def close(self):
        self.client.close()

    def insert(self, json_data):
        """Insert JSON data into the database.

        This method is used to insert the JSON data into the database. While the
        `json_data` is first verified if it is valid, else an error is raised.
        """
        # Handle this error
        # pymongo.errors.DuplicateKeyError
        if isinstance(json_data, dict):
            return self.collection.insert_one(json_data).inserted_id
        elif isinstance(json_data, list):
            return self.collection.insert_many(json_data).inserted_ids

    def insert_from_file(self, file_path):
        """Insert JSON data into the database using a file path.

        Load JSON data into database using a local json file.
        """
        with open(file_path) as file:
            file_data = json.load(file)
        return self.insert(file_data)

    def get(self, _id):
        """Return json data from the given id
        """
        query = {"_id": _id}
        data_query = self.collection.find_one(query)
        return data_query

    def update(self, _id, value):
        """Update the json data of a given id based on the given value
        """
        query = {"_id": _id}
        new_value = {"$set": value}
        self.collection.update_one(query, new_value)

    def delete(self, _id):
        """Delete json data in the databased for a given id
        """
        query = {"_id": _id}
        self.collection.delete_one(query)

    def __str__(self):
        values = ""
        for value in self.collection.find({}):
            values = values + "\n" + str(value)

        return values
