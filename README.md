# Prueba Tecnia
Readme de la prueba técnica.


## Objetivo
La base de datos contiene datos sobre películas, son datos inventados. Hay 5 nodos, películas o movies, usuarios, actores, directores e industrias. Las relaciones son actores con películas, según han actuado en ellas. Directores con películas según las han dirigido, industrias con películas según las han producido y usuarios con películas según las han puntuado. 

El objetivo es, dado un usuario predecir qué películas le gustarán más según las que ya ha visto y puntuado. Se le asigna un porcentaje de posibilidad de que le gusten al usuario, basándose en la puntuación que otros usuarios similares le asignaron en un pasado además de el género de la película.

Para encontrar un usuario parecido al que se le quiere hacer la recomendación se construye un árbol de decisión. El cual se usa para encontrar el usuario/grupo de usuarios más parecido que hay al que le queremos hacer la recomendación. Recuperamos las películas que le/les gustaron a estos usuarios y calculamos la probabilidad de que le gusten a este usuario de forma personalizada, estas películas son las que se muestran al usuario ordenadas por probabilidad de que le gusten.

Estas fases son las de Retrieval, Reuse y Revise dentro del Case-Based Reasoning para recomendar al usuario.

Por último falta la fase de Retain, para la cual se creó una función con la que el usuario puede puntuar nuevas películas y así el sistema puede ampliar su conocimiento y los casos que tiene.
 
## Environment
Se empleó la versión de Python 3.8.5.
Para la base de datos de grafos se utilizó Neo4J y su versión en escritorio. Se adjunta un archivo en este repositorio para llenar la base de datos de información, es el archivo "database_pruebaTecnica.cypher". Este archivo se carga en la aplicación de escritorio de Neo4J o se copia su contenido dentro y la base de datos estará lista.
 
Otro archivo es el "config.txt", en este archivo se introducen la uri, el user y la password de la base de datos. Se deberán modificar los valores para poner los datos de quien quiera ejecutar el programa.
 
