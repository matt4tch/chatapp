import sqlite3
from datetime import datetime

# CONSTANTS

FILE = "messages.db"

class DataBase:
    """
    used to interface with the local sqlite3 database
    """
    def __init__(self):
        """
        try to connect to the file and create a cursor object
        """
        self.conn = sqlite3.connect(FILE)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        create a new database table if one doesn't already exist
        :return: None
        """
        query = f"""CREATE TABLE IF NOT EXISTS Messages
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT, date Date)"""
        self.cursor.execute(query)
        self.conn.commit()
    
    def get_all_messages(self, limit=100, name=None):
        """
        returns all messages
        :param limit: int
        :return: list[dict]
        """

        # query for messages in sorted order by date
        if not name:
            query = f"SELECT * FROM (SELECT * FROM Messages ORDER BY date LIMIT ?) ORDER BY DATE DESC"
            self.cursor.execute(query, (limit,))
        else:
            query = f"SELECT * FROM (SELECT * FROM Messages WHERE NAME = ? ORDER BY date LIMIT ?) ORDER BY DATE DESC"
            self.cursor.execute(query, (name, limit))

        result = self.cursor.fetchall()

        results = []
        for row in result:
            data = {"name": row[1], "message": row[2], "time": str(row[3])}
            results.append(data)

        return results
    
    def save_message(self, name, msg):
        """
        saves the given message in the table
        :param name: str
        :param msg: str
        :param time: datetime
        :return: None
        """
        query = f"INSERT INTO Messages(name, message, date) VALUES (?, ?, ?)"
        self.cursor.execute(query, (name, msg, datetime.now()))
        self.conn.commit()

    def close(self):
        """
        close the database connection
        :return: None
        """
        self.conn.close()
        