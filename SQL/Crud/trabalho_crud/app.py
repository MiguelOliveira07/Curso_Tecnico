# requisitos|:
    
#     ra (texto, não pode repetir, preenchimento obrigatório e ter exatamente 6 caracteres);
    
#     data_nascimento (texto, preenchimento obrigatório, no formato: 'DD-MM-YYYY');

#     curso (texto, preenchimento obrigatório).

import sqlite3
from verificação_dados import validar_nome, validar_ra, validar_curso

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
                ra TEXT NOT NULL UNIQUE,
                data_nascimento TEXT NOT NULL,
                curso TEXT NOT NULL
            )
        '''
        )
    except:
        print('Erro ao criar tabela!')


def inserir_pessoa(nome, ra, data_nascimento, curso):
    conn = conectar()
    try:
        conn.execute(
            '''
            INSERT INTO pessoas (nome, ra, data_nascimento, curso)
            VALUES (?, ?, ?, ?)''',
            (nome, ra, data_nascimento, curso),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print("RA já cadastrado!")
    finally:
        conn.close()


nome = validar_nome()
ra = validar_ra()
data_nascimento = validar_nascimento()
curso = validar_curso()

inserir_pessoa(nome=nome, ra=ra, data_nascimento=data_nascimento, curso=curso)