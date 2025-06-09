class Verificação_dados:
    def __init__(self):
        pass

    def validar_nome(self,mensagem='Insira seu nome: '):
        while True:
            nome = input(mensagem).strip()
            if nome:
                if nome.isalpha():
                    if len(nome) < 3:
                        print("O nome deve ter no mínimo 3 caracteres")
                    elif len(nome) > 50:
                        print("O nome deve ter no máximo 50 caracteres")
                    else:
                        return nome
                else:
                    print('O nome deve conter apenas letras!')
            else:
                print("O nome não pode ficar em branco!")
    

    def validar_idade(self, mensagem='Digite sua idade: '):
        while True:
            idade = input(mensagem).strip()
            if idade:
                if idade.isnumeric():
                    idade = int(idade)
                    if idade >= 18 and idade < 100:
                        return idade
                    print('Informe a idade corretamente')
                else:
                    print("A idade deve conter apenas números!")
            else:
                print("A idade não pode ficar em branco!")


    def validar_cpf(self, mensagem='Digite seu cpf: '):
        while True:
            cpf = input(mensagem).strip()
            if cpf:
                cpf = cpf.replace('.', '').replace('-', '')
                if cpf.isnumeric():
                    if len(cpf) == 11:
                        return cpf
                    print("Número de caracters não satisfeitos [ 11 ]!")
                else:
                    print("O cpf deve conter apenas números!")
            else:
                print("O cpf não pode ficar em branco!")
