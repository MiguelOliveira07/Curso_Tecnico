class calculadora:
    def __init__(self, num1, num2):
        self.num_1 = num1
        self.num_2 = num2
    
    def somar(self):
        soma = self.num_1 + self.num_2
        print(f'A # dos seus números são: {soma}')

    def subtrair(self):
        subtracao = self.num_1 - self.num_2
        print(f'A # dos seus números são: {subtracao}')

    def multiplicação(self):
        multiplicacao = self.num_1 * self.num_2
        print(f'A # dos seus números são: {multiplicacao}')

    def divisão(self):
        divisao = self.num_1 / self.num_2
        print(f'A # dos seus números são: {divisao}')
    
numeros = calculadora(10, 20)

numeros.somar()
numeros.subtrair()
numeros.multiplicação()
numeros.divisão()