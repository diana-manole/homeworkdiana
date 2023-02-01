from flask import flask
import mysql.connector


class DataHelp:
    def __init__(self):
        self.findb = mysql.connector.connect(
            host="localhost", user="python", password="!QA2ws3ed=-2"
        )
        # self.cursor = self.findb.cursor()

    def executeSomeQuery(self, query):
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def querywithCommit(self, query):
        self.cursor = self.findb.cursor()
        self.cursor.execute(query)
        self.findb.commit()
        self.cursor.close()
        return
