from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

from .. import config

class Database(object):
    def __init__(self):
        self.client = MongoClient(config['db']['url'])
        self.db = self.client[config['db']['name']]

    def insert(self, element, collection_name):
        pass

    def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):
        pass

    def find_by_id(self, id, collection_name):
        pass

    def update(self, id, element, collection_name):
        pass

    def delete(self, id, collection_name):
        pass