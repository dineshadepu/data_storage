# Basic CRUD API using pymongo
## Overview


## Installation

### Prerequisites

We need python 3.11.9 and mongod database server which can be installed by
following the instructions at:
```
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
```


### Installing the package

First clone the repository from github by running:

```
git clone https://github.com/dineshadepu/data_storage
```

Then change the directory to the package folder by:

```
cd data_storage
```

We need `pymongo` package to interact with `mongod` database. Which can be
installed by running:
```
pip install -r requirements.txt
```

Finally, the current package can be installed by running:
```
python setup.py develop
```

Before using the package we need `mongod` server to be up and running, which
can be started by running the following command in the terminal:

```
sudo systemctl start mongod
```


### Running the tests

To run the tests, change to the tests directory and execute
```
	python -m unittest -v
```



## Usage

We first create a database and a collection in the mongod using the `MyData`
class provided by the current package:
```
from data_storage.api import MyData
database_name = "db_1"
collection_name = "collection"
data = MyData(database=database_name, collection=collection_name)
```

After the database and corresponding collection is created, we insert the `json`
data into the data base by:
```
json_data = {"name": "John", "address": "Highway 37"}
idx = data.insert(json_data)
```
Or one can insert by passing a file, which has json data by:
```
file_path = "path_to_json_file.json"
idxs = data.insert_from_file(file_path)
```
The `insert` method will handle cases where the json data being inserted is a
single `json` data or a list of `json` data.

We can retrieve (get) the data from the database from a given id, this can be
done by:
```
value = data.get(idx)
```

We can update the data in the database given the id and the
updated values as:
```
update_value = {"name": "Dinesh", "address": "Warangal"}
data.update(id, update_value)
```

We can delete data corresponding to the given id from the database by:
```
data.delete(id)
```
