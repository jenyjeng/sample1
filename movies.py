from flask import Flask,jsonify, request
app = Flask(__name__)
movies = [

    {
        "name": "Hatty Potter",
        "actors": ["Daniel Radcliffe", "Emma Watson"],
        "genres": ["Fantasy"]
    },
    {
        "name": "Big Mouth",
        "actors": ["Lee Jong-Suk", "Im Yoon-ah"],
        "genres": ["Drama, Crimes"]
    },
]
@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def addMovies():
    movies = request.get_json()
    movies.append(movies)
    return {'id' : len(movies)},200

if __name__ == '__main__':
    app.run()