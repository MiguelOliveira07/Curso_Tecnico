import sqlite3
import validators
from Crud.verificação_dados import Verificação_dados

# Conecta ao banco de dados (cria se não existir)
conexao = sqlite3.connect('clientes.db')
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conexao.commit()

def menu():
    print("\n--- MENU CLIENTES ---")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Atualizar cliente")
    print("4. Excluir cliente")
    print("5. Sair")
    return input("Escolha: ")

def cadastrar():

    nome = Verificação_dados.validar_nome('Digite seu nome: ')
    email =Verificação_dados.validar_email('Digite seu email: ')
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    print("Cliente cadastrado!")

def listar():
    cursor.execute("SELECT id, nome, email FROM clientes")
    for cliente in cursor.fetchall():
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

def atualizar():
    id_cliente = input("ID do cliente: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, id_cliente))
    conexao.commit()
    print("Cliente atualizado!")

def excluir():
    id_cliente = input("ID do cliente: ")
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    print("Cliente excluído!")

# Programa principal
while True:
    opcao = menu()
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

# Fecha a conexão ao sair
conexao.close()  