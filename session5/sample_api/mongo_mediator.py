import json
from dataclasses import field
from typing import List

from bson import json_util
from pymongo import MongoClient


class MongoMediator:
    def __init__(self, conn_string: str = None,
                 collection_name: str = "general"):
        self.__client = MongoClient(conn_string)
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

        db_result = list(self.__client.bcr_base[self.__collection_name].
                         find(search_query, projection))

        return db_result

    def get_by_id(self, doc_id):
        """Get a document from the database by ID.
        Args:
            doc_id: string - The id for the document you want to get.
        Returns:
            dict: response - The document from the database.
        Raises:
            None.
        Examples:
              Typical usage example:
                  id = 1
                  mongo = MongoMediator(conn_string, collection_name)
                  response = mongo.get_by_id(id=id)
        """
        search_query = {"city_id": doc_id}
        projection = {"_id": 0}

        db_result = list(self.__client.bcr_base[self.__collection_name].
                         find(search_query, projection))

        response = json.loads(json_util.dumps({"result": db_result}))

        return response

    def insert_one(self, document: dict = None):
        """Insert one document into the currently set collection.
        Args:
            document: dict - The document you want inserted into the
            repositories.
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
        self.__client.bcr_base[self.__collection_name].insert_one(document)

    def insert_many(self, documents: List[dict] = field(default_factory=list)):
        """Insert many documents into the currently set collection.
        Args:
            documents: List[dict] - The documents you want inserted into the
            repositories.
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
        self.__client.bcr_base[self.__collection_name].insert_many(documents)

    def delete_by_id(self, document_id):
        """Delete one document by ID.
        Args:
            document_id: int - The ID of the document to be deleted.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  document_id = 1
                  mongo.delete_by_id(document_id)
        """
        self.__client.bcr_base[self.__collection_name].delete_one(
            {"city_id": document_id})

    def update_by_id(self, document_id, city, population):
        """Update one document by ID.
        Args:
            document_id: int - The ID of the document to be deleted.
            city: str - The city name.
            population: int - The population of the city.
        Returns:
            None.
        Raises:
            None.
        Examples:
              Typical usage example:
                  mongo = MongoMediator(conn_string, collection_name)
                  document_id = 1
                  city = 'x'
                  population = 1000
                  mongo.update_by_id(document_id, city, population)
        """
        self.__client.bcr_base[self.__collection_name].update_one(
            {
                "city_id": document_id
            },
            {
                "$set": {
                    "city": city,
                    "population": population
                }
            }
        )
