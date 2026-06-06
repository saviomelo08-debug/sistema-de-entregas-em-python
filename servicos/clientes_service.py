from modelos.cliente import Cliente
from typing import List, Optional

class ClienteService:
    """Concentra as regras de negócio associadas aos Clientes."""
    
    def __init__(self):
        self.__clientes: List[Cliente] = []

    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str, endereco: str) -> Cliente:
        if self.buscar_por_cpf(cpf):
            raise ValueError("Um cliente com este CPF já está cadastrado.")
        
        novo_cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(novo_cliente)
        return novo_cliente

    def listar_clientes(self) -> List[Cliente]:
        return self.__clientes

    def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None