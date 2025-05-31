import sqlite3
from verificação_dados import validar_nome, validar_idade, validar_cpf

def conectar():
    try:
        conn = sqlite3.connect('banco.db')
    except:
        print('Erro ao criar/conectar o banco!')
    else:
        return conn

   

def criar_tabela():
    try:
        conectar().execute(
            '''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cpf TEXT NOT NULL UNIQUE
            )
        '''
        )
    except:
        print('Erro ao criar tabela!')


def inserir_pessoa(nome, idade, cpf):
    conn = conectar()
    try:
        conn.execute(
            '''
            INSERT INTO pessoas (nome, idade, cpf)
            VALUES (?, ?, ?)''',
            (nome, idade, cpf),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print("CPF já cadastrado!")
    finally:
        conn.close()


nome = validar_nome()
idade = validar_idade()
cpf = validar_cpf()

inserir_pessoa(nome=nome, idade=idade, cpf=cpf)