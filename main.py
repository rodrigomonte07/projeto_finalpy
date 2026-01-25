import mysql.connector
from flask import Flask, jsonify, request
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'senha',
    database= 'estoque_loja'
)

@app.route("/produtos", methods= ['GET'])
def ver_estoque():
    aba = conexao.cursor(dictionary=True)
    aba.execute("SELECT * FROM produtos")
    lista_produtos = aba.fetchall()
    aba.close()
    
    return jsonify(lista_produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto(id):
    aba = conexao.cursor(dictionary=True)
    aba.execute("SELECT * FROM produtos WHERE id = %s", (id,))
    produto = aba.fetchone()
    aba.close()
    if not produto:
        return jsonify({"mensagem": "Produto não encontrado"}), 404

    return jsonify(produto)

@app.route("/produtos", methods= ['POST'])
def cadastrar_produto():
    data = request.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    estoque = data.get('estoque')
    preco = data.get('preco')

    if not nome or estoque is None or preco is None:
        return jsonify({"erro": "Dados incompletos"}), 400

    aba = conexao.cursor(dictionary=True)
    consulta = f"""
INSERT INTO produtos (nome, descricao, estoque, preco)
    VALUES
        (%s, %s, %s, %s)
"""
    aba.execute(consulta, (nome, descricao, estoque, preco))
    conexao.commit()
    aba.close()

    return jsonify({"mensagem": f"Produto {nome} cadastrado com sucesso!"})

@app.route("/produtos/<int:id>", methods= ['PATCH'])
def atualizar_produto(id):
    data = request.get_json()

    campos = []
    valores = []

    if 'nome' in data:
        campos.append("nome = %s")
        valores.append(data['nome'])

    if 'descricao' in data:
        campos.append("descricao = %s")
        valores.append(data['descricao'])

    if 'estoque' in data:
        campos.append("estoque = %s")
        valores.append(data['estoque'])

    if 'preco' in data:
        campos.append("preco = %s")
        valores.append(data['preco'])

    if not campos:
        return jsonify({"mensagem": "Nenhum campo para atualizar"}), 400

    valores.append(id)

    consulta = f"""
        UPDATE produtos
        SET {", ".join(campos)}
        WHERE id = %s
    """

    aba = conexao.cursor()
    aba.execute(consulta, valores)
    conexao.commit()
    aba.close()

    return jsonify({"mensagem": "Produto atualizado com sucesso!"})

@app.route("/produtos/<int:id>", methods=['DELETE'])
def excluir_produto(id):
    aba = conexao.cursor(dictionary=True)
    aba.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()
    aba.close()
    
    return jsonify({"mensagem": "Produto removido com sucesso!"})

if __name__ == "__main__" :
    app.run(debug=True)


