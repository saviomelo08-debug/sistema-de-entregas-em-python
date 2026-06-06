from modelos.pessoa import Pessoa

class Cliente(Pessoa):
    """Classe Cliente herdando características da classe Pessoa (Herança)."""
    
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: str):
        super().__init__(nome, telefone)
        self.__cpf = cpf
        self.__endereco = endereco

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco