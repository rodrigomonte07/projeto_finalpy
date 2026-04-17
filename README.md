# API de Gerenciamento de Estoque - Loja

Uma API REST construída com Flask para gerenciar produtos e estoque de uma loja, com suporte a operações CRUD completas.

## 📋 Funcionalidades

- ✅ **Listar todos os produtos** - GET `/produtos`
- ✅ **Buscar produto por ID** - GET `/produtos/<id>`
- ✅ **Cadastrar novo produto** - POST `/produtos`
- ✅ **Atualizar produto** - PATCH `/produtos/<id>`
- ✅ **Excluir produto** - DELETE `/produtos/<id>`

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-CORS** - Habilitação de CORS
- **mysql-connector-python** - Conexão com MySQL

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/rodrigomonte07/projeto_finalpy.git
cd projeto_finalpy
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install flask flask-cors mysql-connector-python
```

### 3. Configure o banco de dados

Certifique-se de ter MySQL instalado e rodando. Atualize as credenciais no arquivo `main.py`:

```python
conexao = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='estoque_loja'
)
```

### 4. Crie a tabela de produtos

Execute este comando no MySQL:

```sql
CREATE DATABASE estoque_loja;

USE estoque_loja;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    estoque INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);
```

## 🚀 Como Usar

### Iniciar o servidor
```bash
python main.py
```

O servidor estará disponível em `http://localhost:5000`

## 📡 Endpoints da API

### 1. Listar todos os produtos
**GET** `/produtos`

**Resposta (200):**
```json
[
    {
        "id": 1,
        "nome": "Produto 1",
        "descricao": "Descrição do produto",
        "estoque": 10,
        "preco": 25.50
    }
]
```

---

### 2. Buscar produto por ID
**GET** `/produtos/<id>`

**Parâmetros:**
- `id` (int, obrigatório) - ID do produto

**Resposta (200):**
```json
{
    "id": 1,
    "nome": "Produto 1",
    "descricao": "Descrição do produto",
    "estoque": 10,
    "preco": 25.50
}
```

**Resposta (404):**
```json
{
    "mensagem": "Produto não encontrado"
}
```

---

### 3. Cadastrar novo produto
**POST** `/produtos`

**Body (JSON):**
```json
{
    "nome": "Novo Produto",
    "descricao": "Descrição opcional",
    "estoque": 15,
    "preco": 49.99
}
```

**Campos obrigatórios:** `nome`, `estoque`, `preco`

**Resposta (200):**
```json
{
    "mensagem": "Produto Novo Produto cadastrado com sucesso!"
}
```

**Resposta (400):**
```json
{
    "erro": "Dados incompletos"
}
```

---

### 4. Atualizar produto
**PATCH** `/produtos/<id>`

**Parâmetros:**
- `id` (int, obrigatório) - ID do produto

**Body (JSON):**
```json
{
    "nome": "Nome Atualizado",
    "preco": 59.99,
    "estoque": 20
}
```

**Nota:** Você pode atualizar um ou mais campos; apenas os campos enviados serão atualizados.

**Resposta (200):**
```json
{
    "mensagem": "Produto atualizado com sucesso!"
}
```

---

### 5. Excluir produto
**DELETE** `/produtos/<id>`

**Parâmetros:**
- `id` (int, obrigatório) - ID do produto

**Resposta (200):**
```json
{
    "mensagem": "Produto removido com sucesso!"
}
```

---

## 🧪 Testando a API

### Usando cURL

```bash
# Listar todos os produtos
curl http://localhost:5000/produtos

# Buscar produto por ID
curl http://localhost:5000/produtos/1

# Cadastrar novo produto
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome":"Produto Teste","estoque":5,"preco":19.99}'

# Atualizar produto
curl -X PATCH http://localhost:5000/produtos/1 \
  -H "Content-Type: application/json" \
  -d '{"preco":29.99}'

# Deletar produto
curl -X DELETE http://localhost:5000/produtos/1
```

### Usando Postman ou Insomnia

Importe a coleção de requests para testar facilmente todos os endpoints.

## ⚠️ Considerações de Segurança

- **Mude a senha padrão** do banco de dados antes de usar em produção
- **Valide e sanitize** todos os inputs do usuário
- **Use variáveis de ambiente** para armazenar credenciais sensíveis
- **Implemente autenticação e autorização** para endpoints de produção
- **Evite usar `debug=True`** em ambiente de produção

## 📝 Estrutura do Projeto

```
projeto_finalpy/
├── main.py           # Arquivo principal com todos os endpoints
├── README.md         # Este arquivo
└── requirements.txt  # Dependências do projeto
```

## 🐛 Possíveis Melhorias

- [ ] Adicionar autenticação JWT
- [ ] Implementar validação mais robusta de dados
- [ ] Adicionar paginação aos endpoints
- [ ] Criar testes unitários
- [ ] Usar variáveis de ambiente para configuração
- [ ] Implementar tratamento de erros mais detalhado
- [ ] Adicionar logging
- [ ] Criar um arquivo de configuração separado

## 📄 Licença

Este projeto está sob licença MIT.

## 👨‍💻 Autor

Criado por **rodrigomonte07**

---

**Última atualização:** 2026-04-17
