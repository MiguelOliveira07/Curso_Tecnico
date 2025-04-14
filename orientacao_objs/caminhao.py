class caminhao:
    def __init__(self, cor, funcao, peso_max, cidade_origem, cidade_destino):
        self.cor_caminhao = cor
        self.funcao_caminhao = funcao
        self.peso_max_caminhao = peso_max
        self.cidade_origem_caminhao = cidade_origem
        self.cidade_destino_caminhao = cidade_destino
        self.status_on = False
        