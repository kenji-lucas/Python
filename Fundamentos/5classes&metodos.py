# Classes & Métodos

class PC:
    def __init__(self, motherboard, cpu, ram, apu):
        self.placa_mae = motherboard
        self.processador = cpu
        self.memoria = ram
        self.placa_de_video = apu

    def Ligar(self):
        print('ON!')

    def Desligar(self):
        print('OFF!')

    def Specs(self):
        print(self.placa_mae, self.processador,
              self.memoria, self.placa_de_video)


pczyza = PC('B450M', 'RYZEN 5 5600G', '16GB', 'VEGA 7')
pczyza.Ligar()
pczyza.Desligar()
pczyza.Specs()