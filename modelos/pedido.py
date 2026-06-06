from modelos.cliente import Cliente
from interfaces.calculo_frete_interface import CalculoFreteInterface

class Pedido:
    """Entidade centralizadora das informações do pedido."""
    
    STATUS_PERMITIDOS = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]

    def __init__(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo_entrega: CalculoFreteInterface):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__status = "Em preparação"
        # Executa o polimorfismo dinamicamente com base na interface injetada
        self.__valor_frete = tipo_entrega.calcular_frete(distancia)

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def peso(self) -> float:
        return self.__peso

    @property
    def distancia(self) -> float:
        return self.__distancia

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, novo_status: str):
        if novo_status in self.STATUS_PERMITIDOS:
            self.__status = novo_status
        else:
            raise ValueError(f"Status inválido. Escolha entre: {self.STATUS_PERMITIDOS}")

    @property
    def valor_frete(self) -> float:
        return self.__valor_frete