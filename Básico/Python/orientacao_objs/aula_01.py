class carro:
    def __init__(self, marca, cor, ano, pais_origem):
        self.marca_car = marca
        self.cor_car = cor
        self.ano_car = ano
        self.__pais_origem_car = pais_origem
        self.ligado = False

    def ligar_carro(self):
            self.ligado = True
            print(f'O carro da marca: {self.marca_car} está ligado!')

    def mostrar_info(self):
        print(f'Marca: {self.marca_car},\ncor: {self.cor_car},\nano: {self.ano_car},\norigem: {self.__pais_origem_car}')


car1 = carro('BMW', 'preto', '1983', 'Alemanha') 
car2 = carro('chevrolett', 'preto', '1983', 'Alemanha') 


car1.mostrar_info()
     