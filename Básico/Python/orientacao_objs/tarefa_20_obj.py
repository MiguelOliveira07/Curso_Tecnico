class Conversao:
    def __init__(self, valor_para_converter):
        self.valor_ = valor_para_converter
        
    def decimal_para_binario(self):
        # Converte um número decimal para binário
        valor = self.valor_
        if valor == 0:
            return '0'
        resultado = []
        while valor >= 1:
            resto = int(valor % 2)
            resultado.append(str(resto))
            valor = valor // 2
        return ''.join(resultado[::-1])

    def decimal_para_octal(self):
        # Converte um número decimal para octal
        valor = self.valor_
        if valor == 0:
            return '0'
        resultado = []
        while valor >= 1:
            resto = int(valor % 8)
            resultado.append(str(resto))
            valor = valor // 8
        return ''.join(resultado[::-1])

    def decimal_para_hexadecimal(self):
        # Converte um número decimal para hexadecimal (até 15)
        valor = self.valor_
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        
        if valor == 0:
            return '0'
        resultado = []
        
        while valor >= 1:
            resto = int(valor % 16)
            if resto >= 10:
                resultado.append(hex_map[resto])
            else:
                resultado.append(str(resto))
            valor = valor // 16
        return ''.join(resultado[::-1])

# Menu para o usuário escolher a conversão
print("Conversor de Números Decimais")
print("1 - Decimal para Binário")
print("2 - Decimal para Octal")
print("3 - Decimal para Hexadecimal")

opcao = input("Escolha uma opção (1-3): ")
valor = int(input("Digite o valor decimal a ser convertido: "))

conversao = Conversao(valor)

if opcao == '1':
    resultado = conversao.decimal_para_binario()
    print(f"Binário: {resultado}")
elif opcao == '2':
    resultado = conversao.decimal_para_octal()
    print(f"Octal: {resultado}")
elif opcao == '3':
    resultado = conversao.decimal_para_hexadecimal()
    print(f"Hexadecimal: {resultado}")
else:
    print("Opção inválida!")