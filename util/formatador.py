class Formatador:
    @staticmethod
    def formatar_moeda(valor: float) -> str:
        """Converte números decimais para o formato padrão brasileiro de moeda."""
        return f"R$ {valor:.2f}"

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """Adiciona pontuação de máscara visual padrão para exibição de CPFs."""
        c = "".join(filter(str.isdigit, cpf))
        if len(c) == 11:
            return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"
        return cpf