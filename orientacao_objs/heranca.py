import time

def loading_pontos(duracao_segundos):
    fim = time.time() + duracao_segundos
    while time.time() < fim:
        for i in range(4):
            pontos = '.' * i
            print(f'\rCarregando{pontos}   ', end='', flush=True)
            time.sleep(0.3)
    print('\nConcluído!')



class Hardware:
    def __init__(self, marca, geracao, ano, fabricante):
        self._marca = marca
        self._geracao = geracao
        self.ano = ano
        self._fabricante = fabricante  
        
        
class Celular(Hardware):
    def __init__(self, marca, geracao, ano, fabricante, carregador, armazenamento):
        super().__init__(marca, geracao, ano, fabricante)
        
        self._carregador = carregador
        self._armazenamento = armazenamento
        
    def ligar(self):
        print('O celular está ligado.')
    
    def desligar(self):
        print('O celular está desliagado.')
        loading_pontos(1)
        print('DEsligado com sucesso!')
        
    def carregar(self):
        print('O celular agora está carregando, portanto, não mexa nele.')
        loading_pontos(5)


class Notebook(Hardware):
    def __init__(self, marca, geracao, ano, fabricante, cabo_rede, RAM):
        super().__init__(marca, geracao, ano, fabricante)

        self._cabo_rede = cabo_rede
        self._RAM = RAM
    
    def verificar_atualizacao(self):
        loading_pontos(5)
        print('Busca por atualizações concluida, tudo certo!')
        
    def conectar_internet(self):
        loading_pontos(5)
        print('Agora você está conectado a internet!')
    
    def rodando_script(self):
        loading_pontos(5)
        print('Script executado, instalaçoes feitas!')
        
        
class Desktop(Hardware):
    def __init__(self, marca, geracao, ano, fabricante, entrada_USB, teclado_conectado, cor):
        super().__init__(marca, geracao, ano, fabricante)

        self._entrada_USB = entrada_USB
        self._teclado_conectado = teclado_conectado
        self._cor = cor
    
    def verificar_entradas(self):
        if self._entrada_USB == ' ':
            print('Não detectamos dispositivos conectados...')
        else:
            print(f'Dispositivo externo conectado: {self._entrada_USB}.')
        
    def conectar_servidor(self):
        loading_pontos(3)
        print('Agora você está conectado ao servidor!')
    
    def carregar_sistema_operacional(self):
        loading_pontos(4)
        print('Sistema operacional carregado!')
        
meu_celular = Celular('sansung', 15, 2025, 'Sansung', 'desconectado', '256G')

# meu_celular.ligar()
# meu_celular.carregar()
# meu_celular.desligar()
    

meu_note = Notebook('Acer', 'I15', '2023', 'Acer', 'Sim', '16GB')

meu_note.conectar_internet()
meu_note.rodando_script()
meu_note.verificar_atualizacao()



meu_desktop =  Desktop('Positivo', '12', '2025', 'Positivo', 'Pen-Drive', 'Sim', 'Preto')

# meu_desktop.carregar_sistema_operacional()
# meu_desktop.conectar_servidor()
# meu_desktop.verificar_entradas()