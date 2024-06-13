"""In this example we will do basic CRUD operations on a database using the
`data_storage` package. The JSON data loaded from an external file.
"""
from data_storage.api import MyData


# Create a database
database_name = "ex_2"
collection_name = "collection"
data = MyData(database=database_name, collection=collection_name)
# print("Data before any insertion")
# print(data)

# Insert json data into the database
# This will stop the program as the data in json_wrong.json is invalid json data
idx = data.insert_from_file("example_data/json_wrong.json")
