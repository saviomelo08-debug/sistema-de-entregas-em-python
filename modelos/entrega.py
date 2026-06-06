from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaComum(CalculoFreteInterface):
    """Implementação Polimórfica da taxa simples de entrega."""
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 1.5

class EntregaExpressa(CalculoFreteInterface):
    """Implementação Polimórfica com taxa majorada."""
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 3.0

class EntregaPremium(CalculoFreteInterface):
    """Implementação Polimórfica com taxa VIP fixa acrescida."""
    def calcular_frete(self, distancia: float) -> float:
        return (distancia * 5.0) + 20.0