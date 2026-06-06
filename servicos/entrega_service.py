from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium
from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaService:
    """Fábrica responsável por instanciar os subtipos polimórficos de entrega."""
    
    @staticmethod
    def obter_tipo_entrega(opcao: int) -> CalculoFreteInterface:
        if opcao == 1:
            return EntregaComum()
        elif opcao == 2:
            return EntregaExpressa()
        elif opcao == 3:
            return EntregaPremium()
        else:
            raise ValueError("Tipo de entrega não reconhecido pelo sistema.")