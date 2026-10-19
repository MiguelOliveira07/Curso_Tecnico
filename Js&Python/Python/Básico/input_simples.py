"""
Olá João!
Voce tem 79 anos ou 948 meses. 
É Graduado. 
Trabalha como Médico, há 45 anos.
Mora distante 4700.0m do seu trabalho.

"""

nome = input("Qual seu Nome? ")
idade = int(input("Qual sua idade? "))
formacao = input("Tem graduação? (sim / não) ")
prof = input("Qual sua profissão? ")
temp = input("A quantos anos trabalho nessa profissão? (anos) ")
dis = float(input("Qual a distância do seu trabalho a a sua casa (Km)? "))

dism= dis * 1000
ida= idade * 12

formado = ''
if formacao == 'sim':
    formado =     "É Graduado"
else:
    formado = 'Não é formado'

print(f"Olá {nome}!\nVocê tem {idade}, cerca de {ida} meses.\n{formado}\nSua profissão é {prof}, atua a cerca de {temp} anos. \nMora a {dism}m do trabalho.")
