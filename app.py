from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'The Data Warehouse toolkit',
        'autor': 'Ralph Kimball'
    },

     {
        'id': 2,
        'titulo': 'Data Structures And Algorithms In Python',
        'autor': 'Michael T. Goodrich'
    },

     {
        'id': 3,
        'titulo': 'Designing Data-Intensive Applications',
        'autor': 'Martin Kleppmann'
    }
]

#Consultar todos os livros

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)


#Editar livro

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir livro
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)



#rodar app
app.run(port=5000,host='localhost',debug=True)