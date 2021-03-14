from CreateDataframe import Dataframe
from MyDecissionTree import my_decission_tree


class adapter_and_reviser():
    def __init__(self,metric='cosine'):
        self.metric=metric
    def recommend_user(self, user_id):
        data=Dataframe()
        myData, relations = data._get_actual_user_punctuations(user_id)
        myData2, relations2 = data._get_dataframeuser_and_films(user_id)
        X, Y = data.create_my_list_from_dataframe(myData2)
        myDecissionTree = my_decission_tree()
        myDecissionTree._fit(X, Y)
        X_new = data.create_my_list_from_dataframe(myData)
        y_pred = myDecissionTree._predict(X_new[0])
        the_favorite_movies = data.get_user_favorite_movies(y_pred[0])
        movies_already_seen = data.get_user_all_movies(user_id)
        all_films = data.get_all_films()
        list_movies_seen = movies_already_seen['m.title'].tolist()
        all_films.drop(all_films[all_films['m.title'].isin(list_movies_seen)].index, inplace=True)
        return self.calculate_most_similar_films(movies_already_seen,the_favorite_movies,all_films)
    def calculate_most_similar_films(self,films_user,films_user_similar, all_films):
        data=Dataframe()
        films_to_compare=data.combine_dataframes(films_user_similar,all_films)
        films_to_compare.drop(films_to_compare[films_to_compare['m.title'].isin(films_user['m.title'].tolist())].index, inplace=True)
        films_user=films_user.sort_values(['p.score'],ascending=False)
        #ordered_dataframe = films_to_compare.sort_values(['m.genre', 'p.score'], ascending=False)
        j=0
        list_of_genres=films_user['m.genre'].tolist()
        if len(list_of_genres)>0:
            for i in list(set(list_of_genres)):
                if j != 0:
                    first_recommendation = films_to_compare.loc[films_to_compare['m.genre'] == i]
                    df = df.append([first_recommendation])
                else:
                    df = films_to_compare.loc[films_to_compare['m.genre'] == i]
                j=j+1
            first_recommendation = films_to_compare.loc[films_to_compare['m.genre'] == films_user['m.genre'][0]]
            films_to_compare.append([first_recommendation])
        else:
            df=films_to_compare
        df=self.assign_like_probability(list_of_genres, df)
        df = df.sort_values(['like probability'], ascending=False)
        df=df.to_dict('records')
        data={
            "recommendations":df
        }
        return data
    def assign_like_probability(self, list_genres, dataframe):
        likeliness_prob = []
        if len(list_genres) > 0:
            if len(list_genres) > 1:
                a = 0
                first_genre = list_genres[0]
                second_genre = list_genres[1]
                score_list = dataframe["p.score"].tolist()
                genre_list = dataframe["m.genre"].tolist()
                for genre,score in zip(genre_list , score_list):
                    if genre == first_genre:
                        likeliness_prob.append((score+2) / 7)
                    elif genre == second_genre:
                        likeliness_prob.append((score+1) / 7)
                    else:
                        likeliness_prob.append(score/7)
            else:
                first_genre = list_genres[0]
                score_list = dataframe["p.score"].tolist()
                genre_list = dataframe["m.genre"].tolist()
                for genre, score in zip(genre_list, score_list):
                    if genre == first_genre:
                        likeliness_prob.append((score + 1.5) / 6.5)
                    else:
                        likeliness_prob.append(score / 6.5)
        else:
            score_list = dataframe["p.score"].tolist()
            genre_list = dataframe["m.genre"].tolist()
            for genre, score in zip(genre_list, score_list):
                likeliness_prob.append(score / 5)
        dataframe=dataframe.drop(columns=['p.score'])
        dataframe['like probability']=likeliness_prob
        return dataframe
