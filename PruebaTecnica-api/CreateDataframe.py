import pandas as pd
import DB
import numpy as np

myscore=3.0
class Dataframe:
    def __init__(self):
        self.connection=DB.my_movie_database()
    def _get_data_user(self,user):
        Query="MATCH(n:User) WHERE n.id={} RETURN n".format(str(user))
        return self.connection.execute_query(Query)
    def _get_users(self):
        Query = "MATCH(n:User) RETURN n"
        return self.connection.execute_query(Query)
    def _get_dataframeuser_and_films(self,user):
        if user!=None:
            Query="MATCH p=(n)-[r:HASPUNCTUATED]->(m) WHERE n.id<>{} RETURN n.name, r.score, m.title, m.genre".format(str(user))
        else:
            Query = "MATCH p=(n)-[r:HASPUNCTUATED]->(m) RETURN n.name, r.score, m.title, m.genre"
        relations = self.connection.execute_query(Query)
        df = pd.DataFrame([dict(row) for row in relations])
        return df, relations
    def _get_actual_user_punctuations(self, user):
        userToRecommend = "MATCH p=(n)-[r:HASPUNCTUATED]->(m) WHERE n.id={} RETURN n.name, r.score, m.title, m.genre".format(str(user))
        relations = self.connection.execute_query(userToRecommend)
        df = pd.DataFrame([dict(row) for row in relations])

        return df, relations
    def create_my_list_from_dataframe(self,dataframe):
        Query = "MATCH (m:Movie) RETURN m.title"
        relations = self.connection.execute_query(Query)
        newDataFrame=dataframe.pivot(index="n.name", columns="m.title", values="r.score").fillna(2.5)
        newDataFrame.reset_index(inplace=True)
        newDataFrame = newDataFrame.rename_axis(None, axis = 1)
        for serie in relations:
            if(serie['m.title'] not in newDataFrame.columns.tolist()):
                newDataFrame[serie['m.title']] = pd.Series(None, index=newDataFrame.index).fillna(2.5)
        mylist=newDataFrame.loc[:,newDataFrame.columns.tolist()[1:]].values.tolist()
        mylisty=newDataFrame["n.name"].values.tolist()

        return mylist, mylisty
    def insert_punctuation(self,punctuation):
        Query="MATCH (u:User), (m:Movie) WHERE u.name='%s' AND m.title='%s' MERGE (u)-[:HASPUNCTUATED{score:%f}]->(m)" %(punctuation['name'], punctuation['movie'],punctuation['punctuation'])
        self.connection.execute_write_query(Query)

    def get_user_favorite_movies(self, user):
        query="MATCH (user:User{name:'Fer1'})-[p:HASPUNCTUATED]->(m:Movie) WHERE p.score>%d RETURN m.title, m.genre, p.score" %(myscore)
        relations=self.connection.execute_query(query)
        df = pd.DataFrame([dict(row) for row in relations])
        return df
    def get_user_all_movies(self,user):
        query = "MATCH (user:User{id:%d})-[p:HASPUNCTUATED]->(m:Movie) RETURN m.title, m.genre, p.score" %(user)
        relations = self.connection.execute_query(query)
        df = pd.DataFrame([dict(row) for row in relations])
        return df
    def get_all_films(self):
        query="MATCH(m:Movie) RETURN m.title, m.genre"
        relations = self.connection.execute_query(query)
        df = pd.DataFrame([dict(row) for row in relations])
        return df
    def combine_dataframes(self, dataframe1, dataframe2):
        result = pd.merge(dataframe1, dataframe2, how="outer", on=["m.title", "m.genre"])
        return result.fillna(2.5)
    # dataframe2['p.score']=dataframe1['p.score']
    # return dataframe2.fillna(2.5)
