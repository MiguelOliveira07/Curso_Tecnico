class Caminhao:
    def __init__(self, cor, tarefa, peso_max, peso_atual,cidade_destino ):
        self.cor_caminhao = cor
        self.funcao_caminhao = tarefa
        self.peso_max_caminhao = peso_max
        self.peso_atual_caminhao = peso_atual
        self.cidade_destino_caminhao = cidade_destino
        
        self.status_on = False
        
    def ligar(self):
        self.status_on = True
        print('O caminhão está ligado')
    
    def acelerar(self, potencia_aceleração):
        p = potencia_aceleração * 10
        if p >= 101:
            print('O caminhão não irá acelerar mais, limite da via alcançado [ 100 km/h ] !')
            p = 100    

        print(f'O caminhão está acelerando, {p}km/h.')
    
    def desacelerar(self, potencia_desaceleracao):
        d = potencia_desaceleracao * 10
        if d <= 1:
            print('O caminhão não irá desacelerar mais, mínimo da velocidade alcançado!')
            d = 1   

        print(f'O caminhão está diminuindo sua velocidade em {d}km/h.')
    
    def parar(self):
        print('O caminhão irá desacelerar e parar.')
    
    def desligar(self): 
        self.status_on = False
             
        
truck = Caminhao('preto', 'Transportar minério', '2t', '1t', 'Ouro Branco')

truck.ligar()
truck.acelerar(6)
truck.desacelerar(1)
truck.parar()
truck.desligar()


acelerar = 0
parar = 0
abastecer = 0 
        
        