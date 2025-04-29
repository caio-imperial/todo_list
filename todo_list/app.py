from flask import Flask, redirect

app = Flask(__name__)

lista_de_tarefas = []

tarefa = {
    "titulo": "estudar",
    "descricao": "estudar python",
    "feito": False
}

lista_de_tarefas.append(tarefa)

@app.route("/")
def home():
    return redirect('/api/tarefas')

@app.route("/api/tarefas", methods=['GET'])
def ler_tarefas():
    return lista_de_tarefas