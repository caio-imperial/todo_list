from flask import Flask, redirect, request, render_template

from todo_list.utils import retorna_o_maior_id_de_uma_list

app = Flask(__name__)

lista_de_tarefas = []

tarefa = {
    "id": 1,
    "titulo": "estudar",
    "descricao": "estudar python",
    "feito": False
}

lista_de_tarefas.append(tarefa)

@app.route("/")
def home():
    return redirect('/api/tarefas')

@app.route("/api/tarefas", methods=['POST', 'GET'])
def tarefas():

    if request.form.get("_method") == "DELETE":
        id_tarefa = request.form.get('id')
        for tarefa in lista_de_tarefas:
            if tarefa['id'] == int(id_tarefa):
                lista_de_tarefas.remove(tarefa)
                break

    elif request.form.get("_method") == "PUT":
        id_tarefa = request.form.get('id')
        for tarefa in lista_de_tarefas:
            if tarefa['id'] == int(id_tarefa):
                tarefa['feito'] = not tarefa['feito']
                break

    elif request.method == 'POST':
        nova_tarefa = {}
        nova_tarefa['titulo'] = request.form.get('titulo')
        nova_tarefa['descricao'] = request.form.get('descricao')
        nova_tarefa['feito'] = request.form.get('feito') == 'on'
        nova_tarefa['id'] = retorna_o_maior_id_de_uma_list(lista_de_tarefas) + 1
        lista_de_tarefas.append(nova_tarefa)
    

    
    return redirect('/ui')

@app.route("/ui")
def criar_tarefa_tela():
    return render_template('cria_tarefa.html', tarefas=lista_de_tarefas)