def validar_numero()

class Verificação_dados:
    def __init__(self):
        pass

    def validar_nome(self,mensagem='Insira seu nome: '):
        while True:
            nome = input(mensagem).strip().capitalize()
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
                
    def validar_ra(self, mensagem='Insira seu RA: '):
        while True:
            ra = input(mensagem).strip()
            
            if ra.isnumeric():
                ra = str(ra)
                if len(ra) == 6:
                    pass
                else:
                    print('O RA deve ter exatamente 6 números!')
            else:
                print('O RA deve conter apenas números (6)!')

    def validar_nascimento(self, mensagem='Digite sua data de nascimento: [dd-mm-yyyy] '):
        while True:
            data = input(mensagem).strip()

            if data.isnumeric():
                data = str(data)
                if len(data) == 8:
                    pass
                else:
                    print('A data está com menos números que o esperado (se necessário, acrescente o 0)')
            else:
                print('A data deve conter apenas números!')
              
    def validar_curso(self, mensagem='Selecione o seu curso =>\n [ 0 ] Informática\n [ 1 ] Segurança de Trabalho\n [ 2 ] Enfermagem\n [ 3 ] Administração\n=============================='):
        while True:
            curso_selecionado = input(mensagem)
            cursos = {0:'Informática', 1:'Segurança do trabalho', 2:'Enfermagem', 3:'Administração'}
            
            if curso_selecionado <= 3 or curso_selecionado >= 0:
               
            else:
                print('Você não selecionou uma opção viável!')
                
                
            

            

        