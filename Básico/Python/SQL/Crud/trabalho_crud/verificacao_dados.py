def validar_numero(valor, minimo=0, maximo=3):
    try:
        valor = int(valor)
        if minimo <= valor <= maximo:
            return True
        else:
            print(f"Digite um número entre {minimo} e {maximo}.")
            return False
    except ValueError:
        print("Você deve digitar apenas números.")
        return False

class VerificacaoDados:
    def __init__(self):
        pass

    def validar_nome(self, mensagem='Insira seu nome: '):
        while True:
            nome = input(mensagem).strip().capitalize()
            if nome:
                if nome.isalpha():
                    if len(nome) < 3:
                        print("O nome deve ter no mínimo 3 caracteres.")
                    elif len(nome) > 50:
                        print("O nome deve ter no máximo 50 caracteres.")
                    else:
                        return nome
                else:
                    print('O nome deve conter apenas letras!')
            else:
                print("O nome não pode ficar em branco!")

    def validar_ra(self, mensagem='Insira seu RA: '):
        while True:
            ra = input(mensagem).strip()
            if ra.isnumeric():
                if len(ra) == 6:
                    return ra
                else:
                    print('O RA deve ter exatamente 6 números!')
            else:
                print('O RA deve conter apenas números (6)!')

    def validar_nascimento(self, mensagem='Digite sua data de nascimento: [ddmmaaaa] '):
        while True:
            data = input(mensagem).strip()
            if data.isnumeric():
                if len(data) == 8:
                    return data
                else:
                    print('A data deve conter 8 dígitos (ex: 01012000).')
            else:
                print('A data deve conter apenas números!')

    def validar_curso(self, mensagem='Selecione o seu curso =>\n [ 0 ] Informática\n [ 1 ] Segurança do Trabalho\n [ 2 ] Enfermagem\n [ 3 ] Administração\n==> '):
        cursos_switch = {
            0: "Informática",
            1: "Segurança do Trabalho",
            2: "Enfermagem",
            3: "Administração"
        }

        while True:
            escolha = input(mensagem).strip()
            if validar_numero(escolha, 0, 3):
                escolha = int(escolha)
                return cursos_switch.get(escolha)
            else:
                print("Opção inválida! Tente novamente.")
