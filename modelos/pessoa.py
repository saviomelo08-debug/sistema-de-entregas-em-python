class Pessoa:
    """Superclasse abstrata base para representação de entidades humanas."""
    
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome          # Atributo privado (Encapsulamento)
        self.__telefone = telefone  # Atributo privado (Encapsulamento)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone