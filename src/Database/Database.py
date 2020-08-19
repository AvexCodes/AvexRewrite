import sqlite3 as sqli
from Utils.Logger import Logger

from Utils.Cache import tiers_cache

class DatabaseHandler:
    def __init__(self, db: str):
        self.db = db
        self.logger = Logger(write=False)
        self.c = ""

    def connect(self):
        try:
            self.conn = sqli.connect(self.db)
            self.c = self.conn.cursor()
        except Exception as e:
            Logger.error(name="DB", output=e)

    def execute(self, sql: str=None):
        if sql is None:
            return False

        try:
            self.c.execute(sql)
            return True
        except Exception as e:
            Logger.error(name="DB", output=e)
            return False


    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            Logger.error(name="DB", output=e)
            return False

    def close(self):
        try:
            self.conn.close()
            return True
        except Exception as e:
            Logger.error(name="DB", output=e)
            return False


