class Veiculo:
    def __init__(self, modelo, ano, preco_diaria):
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria
        self.alugado = False

    def alugar(self):
        if not self.alugado:
            self.alugado = True
            print(f"{self.modelo} alugado com sucesso!")
        else:
            print(f"{self.modelo} já está alugado.")

    def devolver(self):
        if self.alugado:
            self.alugado = False
            print(f"{self.modelo} devolvido com sucesso!")
        else:
            print(f"{self.modelo} não está alugado.")

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco_diaria, cor, marca, transmissao, tipo_combustivel):
        super().__init__(modelo, ano, preco_diaria)
        self.cor = cor
        self.marca = marca
        self.transmissao = transmissao
        self.tipo_combustivel = tipo_combustivel

    def __str__(self):
        return (f"Modelo: {self.modelo}, Ano: {self.ano}, Preço Diária: {self.preco_diaria}, "
                f"Cor: {self.cor}, Marca: {self.marca}, Transmissão: {self.transmissao}, "
                f"Tipo Combustível: {self.tipo_combustivel}")

class Locadora:
    def __init__(self):
        self.veiculos = {}

    def adicionar_veiculo(self, veiculo):
        self.veiculos[veiculo.modelo] = veiculo
        print(f"Veículo {veiculo.modelo} adicionado à locadora.")

    def alugar_veiculo(self, modelo):
        if modelo in self.veiculos:
            veiculo = self.veiculos[modelo]
            veiculo.alugar()
        else:
            print("Veículo não encontrado na locadora.")

    def devolver_veiculo(self, modelo):
        if modelo in self.veiculos:
            veiculo = self.veiculos[modelo]
            veiculo.devolver()
        else:
            print("Veículo não encontrado na locadora.")

# Exemplo de uso
"""
locadora = Locadora()

carro1 = Carro("Fiat Uno", 2018, 100, "Vermelho", "Fiat", "Manual", "Gasolina")
locadora.adicionar_veiculo(carro1)

print(carro1)

locadora.alugar_veiculo("Fiat Uno")
locadora.devolver_veiculo("Fiat Uno")
"""
