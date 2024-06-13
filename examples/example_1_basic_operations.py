"""In this example we will do basic CRUD operations on a database using the
`data_storage` package. The JSON data is given manually rather from a file.
"""
from data_storage.api import MyData


# Create a database
database_name = "ex_1"
collection_name = "collection"
data = MyData(database=database_name, collection=collection_name)
print("Data before any insertion")
print(data)

# Insert json data into the database
json_data = {"name": "John", "address": "Highway 37"}
idx = data.insert(json_data)
print("Data after insertion")
print(data)

# Get the value at the given id
value = data.get(idx)
print(f"The value of the id={idx} is:")
print(value)
print()

# Update it
value = data.get(idx)
update_value = {"name": "Dinesh", "address": "Warangal"}
data.update(idx, update_value)
print("Data after updating the value")
print(data)
data.delete(idx)

print("Data after deletion")
print(data)
data.client.drop_database('ex_1')
