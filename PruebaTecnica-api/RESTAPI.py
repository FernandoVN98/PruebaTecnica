#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flasgger import Swagger
from flasgger.utils import swag_from

from CreateDataframe import Dataframe
from MyRecommenderSystem import adapter_and_reviser

app = Flask(__name__)

app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispecification",
            "route": "/apispec.json"
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/prueba-tecnica/api/v1.0/swagger"
}

swagger = Swagger(app, config=swagger_config)


@app.route('/prueba-tecnica', methods=['GET'])
def index():
    return jsonify()
@app.route('/prueba-tecnica/users', methods=['GET'])#Funciona
def getUsers():
    """
               ---
               responses:
                 200:
                   description: A list of users
                """
    data = Dataframe()
    return jsonify(data._get_users())
@app.route('/prueba-tecnica/users/<int:id>', methods=['GET'])#Funciona
def getUser(id):
    """
           ---
           parameters:
             - in: path
               name: id
               type: integer
               required: true
           responses:
             200:
               description: A single user item
            """
    data = Dataframe()
    toreturn=data._get_data_user(id)
    return jsonify(toreturn)
@app.route('/prueba-tecnica/users/<int:id>/films', methods=['POST'])#Trabajando en el
def punctuate_film(id):
    """
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
            default: 1
          - name: body
            in: body
            required: true
            schema:
              id: Product
              required:
                - name
              properties:
                name:
                  type: string
                  description: The user's name.
                  default: Fer1
                punctuation:
                  type: integer
                  description: punctuation assigned to the film.
                  default: 5.0
                movie:
                  type: string
                  description: title of the movie that is going to be scored.
                  default: The Godfather
        responses:
          200:
            description: The product inserted in the database
        """
    if not request.json:
        abort(400)
    punctuation_to_assign = {
        'name': request.json['name'],
        'punctuation': request.json['punctuation'],
        'movie': request.json['movie']
    }
    data = Dataframe()
    data.insert_punctuation(punctuation_to_assign)
    return jsonify({'task': punctuation_to_assign}), 201
@app.route('/prueba-tecnica/users/<int:id>/films', methods=['GET'])#Trabajando en el
def get_recommended_films(id):
    """
                   ---
                   parameters:
                     - in: path
                       name: id
                       type: integer
                       required: true
                   responses:
                     200:
                       description: User gets films recommend to him/herself
                    """
    adapter=adapter_and_reviser()
    return adapter.recommend_user(id)
if __name__ == '__main__':
    app.run(debug=True)
