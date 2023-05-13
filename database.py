import sqlite3, pickle, base64
from typing import Any

def Serialize(obj):
    return base64.b64encode(pickle.dumps(obj))

def Deserialize(obj):
    return pickle.loads(base64.b64decode(obj))

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, data BLOB)")
        self.conn.commit()

    def insert(self, key, value):
        self.cur.execute("INSERT INTO players VALUES (?, ?)", (key, Serialize(value)))
        self.conn.commit()
    
    def update(self, key, value):
        self.cur.execute("UPDATE players SET data = ? WHERE id = ?", (Serialize(value), key))
        self.conn.commit()
    
    def get(self, key):
        self.cur.execute("SELECT data FROM players WHERE id = ?", (key,))
        return Deserialize(self.cur.fetchone()[0])
    
    def delete(self, key):
        self.cur.execute("DELETE FROM players WHERE id = ?", (key,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
    def doesPlayerExist(self, id):
        self.cur.execute("SELECT * FROM players WHERE id = ?", (id,))
        return self.cur.fetchone() != None