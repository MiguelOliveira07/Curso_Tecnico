import sqlite3
from verificação_dados import validar_nome, validar_idade, validar_cpf

class Conectar_banco:
    def __init__(self):
        pass
    
    def conectar(self):
        try:
            conn = sqlite3.connect('banco.db')
        except:
            print('Erro ao criar/conectar o banco!')
        else:
            return conn
        
    def desconectar(self):
        try:
            conn = sqlite3.close('banco.db')
            print('Banco de dados desconectado!')
        
        except:
            print('Não foi possivel desconectar o banco de dados, tente novamente!')

   

def criar_tabela():
    try:
        Conectar_banco.conectar().execute(
            '''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento INTEGER NOT NULL,
                curso TEXT NOT NULL
            )
        '''
        )
    except:
        print('Erro ao criar tabela!')


def inserir_pessoa(nome, idade):
    conn = Conectar_banco.conectar()
    try:
        conn.execute(
            '''
            INSERT INTO pessoas (nome, idade, cpf)
            VALUES (?, ?)''',
            (nome, idade),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print("CPF já cadastrado!")
    finally:
        conn.close()

        
        
        