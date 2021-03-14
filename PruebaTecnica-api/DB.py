import configparser

from neo4j import GraphDatabase, basic_auth
parser = configparser.ConfigParser()
parser.read("config.txt")
uri=parser.get("database", "uri")
user=parser.get("database", "user")
password=parser.get("database", "password")
class my_movie_database:
    def __init__(self, Uri=uri, User=user, Password=password):
        print(uri)
        self.driver = GraphDatabase.driver(Uri, auth=basic_auth(User, Password))
    def get_instance_of_my_database(self):
        return self.driver.session()
    def execute_query(self,query):
        with self.driver.session() as session:
            values = session.read_transaction(lambda tx: tx.run(query).data())
        return values
    def execute_write_query(self,query):
        with self.driver.session() as session:
            values = session.write_transaction(lambda tx: tx.run(query).data())
        return values
    def close(self):
        self.driver.close()