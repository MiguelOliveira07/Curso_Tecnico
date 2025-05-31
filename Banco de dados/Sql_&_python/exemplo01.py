# importa a biblioteca
import sqlite3

# cria e conecta em um banco de dados
conexao = sqlite3.connect(database='senac.db') 

# executa os comandos SQL e manipula o banco de dados
cursor = conexao.cursor()

# criar tabela
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    ra VARCHAR(6) NOT NULL UNIQUE
)                         
''')

# fazer as alterações no banco
conexao.commit()

# criando dados par as duas colunas
try:
    cursor.execute('''
        INSERT INTO alunos (nome,ra)
        VALUES (?,?)
                ''',('José', 22334455))

    # fazer as alterações no banco
    conexao.commit()
except:
    print('Erro ao criar dados na tabela')
    
cursor.execute('SELECT * FROM alunos')   
linhas = cursor.fetchall()

print(linhas)

for linha in linhas:
    print(linha)
    
# desempacotando a tupla
id, nome, ra = linha
print(f'a ultima linha é: {linha}')

try:
    cursor.execute('''
            UPDATE alunos
            SET nome = ?
            WHERE ra = ?
                ''', ('João Pualo', '69812'))
    conexao.commit()
except:
    print('Erro ao tentar alterar o nome.')
    
try:
    cursor.execute('''
        DELETE FROM alunos
        WHERE ra = ?
                ''', (999532,))
    conexao.commit()
except:
    print('Erro ao excluir dado')

# fechar a conexão com o banco (sempre a ultima coisa a ser feita)
conexao.close()