import os

class Gerenciando_Diretório:
    def __init__(self):
        pass
    
    def criar_pastas(self,url, nome_pasta):
        juncao = os.path.join(url, nome_pasta)
        os.makedirs(juncao)
        

diretorio = Gerenciando_Diretório()

diretorio.criar_pastas("C:\\Users\\999532\\Documents\\Curso_Tecnico\\orientacao_objs\\teste01\\teste02", "teste03")



