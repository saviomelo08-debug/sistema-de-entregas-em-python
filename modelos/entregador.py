from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    """Classe Entregador herdando de Pessoa."""
    
    def __init__(self, nome: str, telefone: str, veiculo: str, cnh: str):
        super().__init__(nome, telefone)
        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self) -> str:
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: str):
        self.__veiculo = veiculo

    @property
    def cnh(self) -> str:
        return self.__cnh