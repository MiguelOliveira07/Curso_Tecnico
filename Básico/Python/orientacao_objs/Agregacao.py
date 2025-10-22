class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
    
    def estudar(self, materia):
        return f"{self.nome} está estudando {materia}"
    
    def fazer_prova(self):
        return f"{self.nome} está realizando uma prova"

class Escola:
    def __init__(self, nome, endereco, diretor):
        self.nome = nome
        self.endereco = endereco
        self.diretor = diretor
        self.alunos = []  # Agregação de alunos
    
    def matricular_aluno(self, aluno):
        self.alunos.append(aluno)
        return f"{aluno.nome} matriculado com sucesso na {self.nome}"
    
    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos]

# Exemplo de uso
aluno1 = Aluno("João Silva", 15, "2023001")
aluno2 = Aluno("Maria Souza", 16, "2023002")
escola = Escola("Escola Municipal", "Rua das Flores, 123", "Carlos Andrade")

print(escola.matricular_aluno(aluno1))
print(escola.matricular_aluno(aluno2))
print("Alunos matriculados:", escola.listar_alunos())
print(aluno1.estudar("Matemática"))


class Colaborador:
    def __init__(self, nome, cargo, salario, id_funcional):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.id_funcional = id_funcional
    
    def trabalhar(self, tarefa):
        return f"{self.nome} está trabalhando em: {tarefa}"
    
    def receber_aumento(self, percentual):
        self.salario *= (1 + percentual/100)
        return f"Novo salário de {self.nome}: R${self.salario:.2f}"

class Empresa:
    def __init__(self, nome, cnpj, ramo, presidente):
        self.nome = nome
        self.cnpj = cnpj
        self.ramo = ramo
        self.presidente = presidente
        self.colaboradores = []  # Agregação de colaboradores
    
    def contratar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)
        return f"{colaborador.nome} contratado como {colaborador.cargo}"
    
    def folha_pagamento(self):
        total = sum(colab.salario for colab in self.colaboradores)
        return f"Total da folha de pagamento: R${total:.2f}"

# Exemplo de uso
colab1 = Colaborador("Ana Costa", "Desenvolvedora", 5500.00, "DEV001")
colab2 = Colaborador("Pedro Santos", "Analista", 4800.00, "ANA002")
empresa = Empresa("Tech Solutions", "12.345.678/0001-99", "Tecnologia", "Roberto Almeida")

print(empresa.contratar_colaborador(colab1))
print(empresa.contratar_colaborador(colab2))
print(empresa.folha_pagamento())
print(colab1.trabalhar("Desenvolvimento de API"))
print(colab2.receber_aumento(10))


class MemoriaRAM:
    def __init__(self, capacidade, velocidade):
        self.capacidade = capacidade  # em GB
        self.velocidade = velocidade  # em MHz
    
    def ler_dados(self):
        return f"Memória RAM {self.capacidade}GB lendo dados a {self.velocidade}MHz"
    
    def gravar_dados(self):
        return f"Memória RAM {self.capacidade}GB gravando dados"

class PlacaMae:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self.memorias = []  # Agregação de memórias RAM
    
    def instalar_memoria(self, memoria):
        if len(self.memorias) < 4:  # Supondo 4 slots
            self.memorias.append(memoria)
            return f"Memória de {memoria.capacidade}GB instalada"
        return "Todos os slots de memória estão ocupados"
    
    def info_memorias(self):
        return f"Total de memória: {sum(mem.capacidade for mem in self.memorias)}GB"

# Exemplo de uso
mem1 = MemoriaRAM(8, 2400)
mem2 = MemoriaRAM(16, 3200)
placa_mae = PlacaMae("B450", "ASUS")

print(placa_mae.instalar_memoria(mem1))
print(placa_mae.instalar_memoria(mem2))
print(placa_mae.info_memorias())
print(mem1.ler_dados())
print(mem2.gravar_dados())