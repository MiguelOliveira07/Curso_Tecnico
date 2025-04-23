import os

class Manipulação_diretório:
    def __init__(self, nome_diretório, pasta_pai):
        self._nome = str(nome_diretório)
        self._pasta_pai = pasta_pai
        
        
    def criar_pasta(self,sub):
        sub = sub
        
        if sub is None:            
            os.chdir(self._pasta_pai)
            os.mkdir(self._nome)
        else:
            os.mkdir(sub + '\\' + self._nome)
        print(sub +'teste')    


teste = Manipulação_diretório('diretório_teste', 'C:/Users/999532/Documents/Curso_Tecnico/orientacao_objs')
teste.criar_pasta('diretório_teste')
