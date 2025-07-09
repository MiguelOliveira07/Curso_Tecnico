class NPC:
    def __init__(self, altura, forca, habilidade_especial):
        self._npc_altura= altura
        self._npc_forca= forca
        self._npc_habilidade_especial= habilidade_especial
        
        self.stelf  = False
        
        
    def atacar(self):
        print(f'Ataque concluido, {self._npc_forca} de dano infligido ao inimigo.')
        
    def correr(self):
        print('O personagem está correndo por 10m')
    
    def ataque_forte(self):
        print(f'{self._npc_forca} de dano infligido + o uso de (a) {self._npc_habilidade_especial} ( 60 de dano )')
        

personagem  = NPC(1.70, 40, 'Flecha flamejante')

personagem.correr()
personagem.atacar()
personagem.ataque_forte()

