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
