class Cpu:
    def __init__(self, frequencia_clock,numero_nucleos,cache,tecnologia_fabricacao,consumo_energia):
        
        self._frequencia_clock = frequencia_clock
        self._numero_nucleos = numero_nucleos
        self._cache = cache
        self._tecnologia_fabricacao = tecnologia_fabricacao
        self._consumo_energia = consumo_energia
        
    def executar_instrucoes(self):
        print('Funções sendo executadas!')

    def aumentar_clock(self):
        print('Aumentando o clock em 5%')

    def verificar_temperatura(self):
        print('Temperatua verificada, está estável')
        
        
        
        
class Gpu:
    def __init__(self, memoria_vram,frequencia_core,tipo_memoria,consumo_eneria):
        
        self.cpu = Cpu(10.2, 3, '10Gb', 'Chinesa','2000mil/h')
        self._memoria_vram = memoria_vram
        self._frequencia_core = frequencia_core
        self._tipo_memoria = tipo_memoria
        self._consumo_eneria = consumo_eneria
        
    def renderizar_video(self):
        print('Vídeo foi renderizao!')

    def ajustar_clock(self):
        print('Clock ajustado.')

    def verificar_utilizacao(self):
        print('Sistema verificada, sem atualizações.')
        
pc = Gpu('16Gb', '2.4', 'Interada','6000mi/h')

# pc.ajustar_clock()
# pc.renderizar_video()
# pc.verificar_utilizacao()
# cpu.executar_instrucoes()



class Motor:
    def __init__(self, potencia, ano, peso):
        self._potencia = potencia
        self._ano = ano
        self._peso = peso
    
    def ligar(self):
        print('O motor está ligado')

    def movimentar(self):
        print('O motor está em movimento agora')
        
    def desligar(self):
        print('O motor irá parar e desligar!')
        
        
class Carro:
    def __init__(self , marca, km):
        self._motor =  Motor('550HP', 2018, '1T')
        self._marca = marca
        self._km = km
    
    def ligar(self):
        print('O carro está ligado')

    def andar(self):
        print('O carro está em movimento agora')
    
    def desligar(self):
        print('O carro irá parar e desligar!')
        
carro = Carro( 'chevrollet', 345.093)

# carro.ligar()
# carro.andar()
# carro.desligar()



class Fonte:
    def __init__(self, potencia, marca, eficiencia):
        self.fonte = Fonte(1000, "Corsair", "80 Plus Gold")
        self.potencia = potencia
        self.marca = marca
        self.eficiencia = eficiencia

    def ligar(self):
        print("Fonte ligada")

    def desligar(self):
        print("Fonte desligada")

    def verificar_eficiencia(self):
        return f"Eficiência: {self.eficiencia}"

    def fornecer_energia(self):
        print(f"Fornecendo {self.potencia}W de energia")


class GPURTX4090:
    def __init__(self, memoria, clock, fabricante, fonte):
        self.memoria = memoria
        self.clock = clock
        self.fabricante = fabricante
        self.fonte = fonte

    def ligar_gpu(self):
        print("GPU RTX 4090 ligada")

    def desligar_gpu(self):
        print("GPU RTX 4090 desligada")
        

    def mostrar_detalhes(self):
        print(f"GPU: {self.fabricante} RTX 4090, {self.memoria}GB, Clock: {self.clock}MHz")

    def usar_gpu(self):
        print("Processando com a GPU RTX 4090")


gpu = GPURTX4090(24, 2520, "NVIDIA")

gpu.ligar_gpu()
gpu.usar_gpu()
gpu.mostrar_detalhes()
gpu.desligar_gpu()
