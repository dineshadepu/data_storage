import pymongo


class MyData():
    def __init__(self, database, collection, json_data=None):
        # mongodb related variables
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[database]
        self.collection = self.database[collection]

        if json_data is not None:
            try:
                self.insert(json_data)
            except:
                print("The Json data is not valid")

    def close(self):
        self.client.close()

    def insert(self, json_data):
        if isinstance(json_data, dict):
            self.collection.insert_one(json_data)
        elif isinstance(json_data, list):
            self.collection.insert_many(json_data)

    def get(self, _id):
        query = {"_id": _id}
        data_query = self.collection.find_one(query)
        return data_query

    def update(self, _id, value):
        # Test if the value is a valid json
        query = {"_id": _id}
        new_value = {"$set": value}
        self.collection.update_one(query, new_value)

    def delete(self, _id):
        # Test if the value is a valid json
        query = {"_id": _id}
        self.collection.delete_one(query)
