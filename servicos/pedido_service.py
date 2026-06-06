from modelos.pedido import Pedido
from modelos.cliente import Cliente
from interfaces.calculo_frete_interface import CalculoFreteInterface
from typing import List, Optional

class PedidoService:
    """Gerencia o ciclo de vida operacional de Pedidos e Entregas."""
    
    def __init__(self):
        self.__pedidos: List[Pedido] = []

    def criar_pedido(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo_entrega: CalculoFreteInterface) -> Pedido:
        if self.buscar_por_codigo(codigo):
            raise ValueError("Já existe um pedido registrado com este código.")
        
        novo_pedido = Pedido(codigo, cliente, peso, distancia, tipo_entrega)
        self.__pedidos.append(novo_pedido)
        return novo_pedido

    def listar_pedidos(self) -> List[Pedido]:
        return self.__pedidos

    def buscar_por_codigo(self, codigo: str) -> Optional[Pedido]:
        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                return pedido
        return None

    def atualizar_status(self, codigo: str, novo_status: str) -> bool:
        pedido = self.buscar_por_codigo(codigo)
        if pedido:
            pedido.status = novo_status
            return True
        return False