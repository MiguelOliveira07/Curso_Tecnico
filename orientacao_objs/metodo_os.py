import os

class Gerenciando_Diretório:
    def __init__(self):
        pass
    
    def criar_pastas(self,url, nome_pasta):
        juncao = os.path.join(url, nome_pasta)
        os.makedirs(juncao)
    
    def editar_nomes(self,url,novo_nome):
        os.rename(url,novo_nome)
    
    def listar(self,diretorio):
        os.remove() 
        

diretorio = Gerenciando_Diretório()

# diretorio.criar_pastas("C:\\Users\\999532\\Documents\\Curso_Tecnico\\orientacao_objs\\teste01\\teste02", "teste03")
# diretorio.editar_nomes("C:\\Users\\999532\\Documents\\Curso_Tecnico\\orientacao_objs\\teste01", "C:\\Users\\999532\\Documents\\Curso_Tecnico\\orientacao_objs\\novo_nome01")



