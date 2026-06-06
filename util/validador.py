import re

class Validador:
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Verifica se o CPF possui exatamente 11 dígitos numéricos."""
        cpf_limpo = re.sub(r'\D', '', cpf)
        return len(cpf_limpo) == 11

    @staticmethod
    def validar_vazio(texto: str) -> bool:
        """Garante que strings enviadas não sejam nulas ou vazias."""
        return not texto or len(texto.strip()) == 0