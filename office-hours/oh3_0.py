import json
import random
from dataclasses import field
from typing import List

from bson import json_util
from pymongo import MongoClient


class MongoMediator:
    def __init__(self, conn_string: str = None, db_name: str = "root", collection_name: str = "general"):
        self.__client = MongoClient(conn_string)
        self.__database_name = db_name
        self.__collection_name = collection_name

    def set_collection(self, collection_name):
        """Sets a collection to store elements for the current object state.
        Args:
            collection_name: string - The collection name you want to be set.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  mongo.set_collection('example_collection')
        """
        self.__collection_name = collection_name

    def get_all(self):
        """Get all documents from the currently set collection.
        Args:
            None.
        Returns:
            List[dict]: response - The list of documents from the repositories.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  response = mongo.get_all()
        """
        search_query = {}
        projection = {"_id": 0}

        db_result = list(self.__client[self.__database_name][self.__collection_name].find(search_query, projection))

        response = json.loads(json_util.dumps(db_result))

        return response

    def insert_one(self, document: dict = None):
        """Insert one document into the currently set collection.
        Args:
            document: dict - The document you want inserted into the repositories.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  document = {
                      'id': 1
                  }
                  mongo.insert_one(document)
        """
        self.__client[self.__database_name][self.__collection_name].insert_one(document)

    def insert_many(self, documents: List[dict] = field(default_factory=list)):
        """Insert many documents into the currently set collection.
        Args:
            documents: List[dict] - The documents you want inserted into the repositories.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  documents = [{
                      'id': 1
                  }]
                  mongo.insert_many(documents)
                  :param documents:
        """
        self.__client[self.__database_name][self.__collection_name].insert_many(documents)

    def delete_one(self, id: str):
        self.__client[self.__database_name][self.__collection_name].delete_one({"_id": id})
        

if __name__ == "__main__": 
    conn_str = "mongodb+srv://bogdan:amilar@general-free.odo4h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # connect to database
    mongo = MongoMediator(conn_string=conn_str, db_name="bcr_base", collection_name="branches")

    # get all data
    data = mongo.get_all()

    import pprint
    pprint.pprint(data)
