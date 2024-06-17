from flask import Flask, make_response, jsonify
from alunos import alunos
from flask_cors import CORS

app = Flask(__name__)  # instaciar a api com nome de app
CORS(app)

@app.route("/alunos", methods=["GET"])  ##informa ao flask que é uma rota
def get_alunos():
    return make_response(jsonify(alunos))
app.run()
