import sqlite3
from verificacao_dados import VerificacaoDados

# Conexão com o banco
def conectar():
    try:
        return sqlite3.connect('banco.db')
    except:
        print('Erro ao conectar ao banco!')
        return None

# Criação da tabela
def criar_tabela():
    conn = conectar()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    ra TEXT NOT NULL UNIQUE,
                    data_nascimento TEXT NOT NULL,
                    curso TEXT NOT NULL
                )
            ''')
            conn.commit()
        except:
            print('Erro ao criar tabela!')
        finally:
            conn.close()

# Inserir pessoa
def inserir_pessoa(nome, ra, data_nascimento, curso):
    conn = conectar()
    try:
        conn.execute(
            'INSERT INTO pessoas (nome, ra, data_nascimento, curso) VALUES (?, ?, ?, ?)',
            (nome, ra, data_nascimento, curso)
        )
        conn.commit()
        print("Cadastro realizado com sucesso!\n")
    except sqlite3.IntegrityError:
        print("RA já cadastrado!\n")
    finally:
        conn.close()

# Listar todos
def listar_alunos():
    conn = conectar()
    try:
        cursor = conn.execute('SELECT * FROM pessoas')
        alunos = cursor.fetchall()
        if alunos:
            for aluno in alunos:
                print(f"ID: {aluno[0]}, Nome: {aluno[1]}, RA: {aluno[2]}, Nascimento: {aluno[3]}, Curso: {aluno[4]}")
        else:
            print("Nenhum aluno cadastrado.")
    finally:
        conn.close()

# Buscar aluno por ID
def buscar_aluno_por_id(id):
    conn = conectar()
    try:
        cursor = conn.execute('SELECT * FROM pessoas WHERE id=?', (id,))
        aluno = cursor.fetchone() # pega a linha seguir e torna uma tupla
        if aluno:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, RA: {aluno[2]}, Nascimento: {aluno[3]}, Curso: {aluno[4]}")
        else:
            print("Aluno não encontrado.")
    finally:
        conn.close()

# Atualizar aluno
def atualizar_aluno(id, nome, ra, data_nascimento, curso):
    conn = conectar()
    try:
        conn.execute(
            '''UPDATE pessoas SET nome=?, ra=?, data_nascimento=?, curso=? WHERE id=?''',
            (nome, ra, data_nascimento, curso, id)
        )
        conn.commit()
        print("Aluno atualizado com sucesso!")
    except:
        print("Erro ao atualizar aluno.")
    finally:
        conn.close()

# Deletar aluno
def deletar_aluno(id):
    conn = conectar()
    try:
        conn.execute('DELETE FROM pessoas WHERE id=?', (id,))
        conn.commit()
        print("Aluno deletado com sucesso!")
    finally:
        conn.close()

# Menu principal
def menu():
    criar_tabela()
    validador = VerificacaoDados()

    while True:
        print('''
============================
    MENU PRINCIPAL
============================
1 - Cadastrar aluno
2 - Listar todos os alunos
3 - Buscar aluno por ID
4 - Atualizar aluno
5 - Deletar aluno
0 - Encerrar programa
''')
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                nome = validador.validar_nome()
                ra = validador.validar_ra()
                nascimento = validador.validar_nascimento()
                curso = validador.validar_curso()
                inserir_pessoa(nome, ra, nascimento, curso)

            case "2":
                listar_alunos()

            case "3":
                id = input("Digite o ID do aluno: ").strip()
                if id.isdigit():
                    buscar_aluno_por_id(int(id))
                else:
                    print("ID inválido.")

            case "4":
                id = input("Digite o ID do aluno a atualizar: ").strip()
                if id.isdigit():
                    nome = validador.validar_nome()
                    ra = validador.validar_ra()
                    nascimento = validador.validar_nascimento()
                    curso = validador.validar_curso()
                    atualizar_aluno(int(id), nome, ra, nascimento, curso)
                else:
                    print("ID inválido.")

            case "5":
                id = input("Digite o ID do aluno para excluir: ").strip()
                if id.isdigit():
                    deletar_aluno(int(id))
                else:
                    print("ID inválido.")

            case "0":
                print("Encerrando o programa...")
                break

            case _:
                print("Opção inválida! Tente novamente.")

# Execução
if __name__ == '__main__':
    menu()
