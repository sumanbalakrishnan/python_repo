"""
Author : Suman Balakrishnan
Date : 20-07-2023

Database handler
"""


import sqlite3


class AppDatabase:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AppDatabase, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        pass

    def get_reader(self):
        pass

    def get_writer(self):
        pass
