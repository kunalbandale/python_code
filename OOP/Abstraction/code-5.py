from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL Database")

    def query(self, sql):
        print(f"MySQL executing: {sql}")


class SQLite(Database):
    def connect(self):
        print("Connected to SQLite Database")

    def query(self, sql):
        print(f"SQLite executing: {sql}")


# Client
db = MySQL()
db.connect()
db.query("SELECT * FROM users")