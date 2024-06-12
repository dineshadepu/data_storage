import unittest
from pymongo.errors import ConnectionFailure
from data_storage.api import MyData


class TestInitializeMyData(unittest.TestCase):
    def setUp(self):
        # Create the database
        database_name = "test_database"
        collection_name = "collection"
        self.data = MyData(database=database_name, collection=collection_name)
        # first insert data into the database
        self.single_json_data = {"_id": 1, "name": "John", "address": "Highway 37"}
        self.data.insert(self.single_json_data)

    def tearDown(self):
        # Create the database
        self.data.client.drop_database('test_database')
        self.data.close()

    def test_read_data_with_correct_id(self):
        # Get the data based on the  id
        value = self.data.get(1)
        self.assertDictEqual(self.single_json_data, value)

    def test_read_data_with_incorrect_id(self):
        # Get the data based on the  id
        value = self.data.get(2)
        self.assertEqual(None, value)

    def test_update_data_with_correct_id(self):
        # Get the data based on the  id
        update_value = {"name": "Dinesh", "address": "Warangal"}
        expected_update_value = {"_id": 1, "name": "Dinesh", "address": "Warangal"}
        self.data.update(1, update_value)
        self.assertDictEqual(expected_update_value, self.data.get(1))

    def test_update_data_with_incorrect_id(self):
        # Get the data based on the  id
        update_value = {"name": "Dinesh", "address": "Warangal"}
        expected_update_value = {"_id": 1, "name": "Dinesh", "address": "Warangal"}
        self.data.update(2, update_value)
        self.assertDictEqual(self.single_json_data, self.data.get(1))

    def test_delete_data_with_correct_id(self):
        # Get the data based on the  id
        self.data.delete(1)
        self.assertEqual(None, self.data.get(1))

    def test_delete_data_with_incorrect_id(self):
        # Get the data based on the  id
        self.data.delete(2)
        self.assertDictEqual(self.single_json_data, self.data.get(1))


if __name__ == '__main__':
    unittest.main()
