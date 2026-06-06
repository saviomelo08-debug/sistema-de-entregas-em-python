from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    """
    Interface que define o contrato abstrato para o cálculo de frete.
    Obrigatório o uso do módulo ABC para garantir a abstração em Python.
    """
    
    @abstractmethod
    def calcular_frete(self, distancia: float) -> float:
        """Calcula o valor do frete com base na distância informada."""
        pass