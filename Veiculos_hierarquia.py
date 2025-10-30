class Veiculo:
    def __init__(self,modelo,marca,cor):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor

class Veiculo_nao_registrado(Veiculo):
    def __init__(self, modelo, marca, cor,sem_placa:None):
        super().__init__(modelo, marca, cor)
        self.sem_placa = sem_placa

class Bicicleta(Veiculo_nao_registrado):
    def __init__(self, modelo, marca, cor, sem_placa,material,marchas):
        super().__init__(modelo, marca, cor, sem_placa)
        self.material = material
        self.marchas = marchas

class Veiculo_registrado(Veiculo):
    def __init__(self, modelo, marca, cor,placa):
        super().__init__(modelo, marca, cor)
        self.placa = placa

class Moto(Veiculo_registrado):
    def __init__(self, modelo, marca, cor, placa,guidao):
        super().__init__(modelo, marca, cor, placa)
        self.guidao = guidao

class Carro(Veiculo_registrado):
    def __init__(self, modelo, marca, cor, placa,portas):
        super().__init__(modelo, marca, cor, placa)
        self.portas = portas

class Carro_combustão(Carro):
    def __init__(self, modelo, marca, cor, placa, portas,tanque):
        super().__init__(modelo, marca, cor, placa, portas)
        self.tanque = tanque

class Carro_eletrico(Carro):
    def __init__(self, modelo, marca, cor, placa, portas,bateria):
        super().__init__(modelo, marca, cor, placa, portas)
        self.bateria = bateria
        
def main():
    bicicleta1 = Bicicleta('Fazer','Yamaha','Vermelha',True,'Aluminio',18)
    moto1 = Moto('Ninja','Kawasaki','Verde','XYZ-123',True)
    carro1 = Carro_combustão('Corolla','Toyota','Prata','ABC-456',4,50)
    carro2 = Carro_eletrico('Model S','Tesla','Branco','ELE-789',4,100) 
    print(vars(bicicleta1))
    print(vars(moto1))
    print(vars(carro1))
    print(vars(carro2))
    
main()