import os

class Menu:
    @staticmethod
    def limpar_tela():
        """Limpa a interface do terminal dinamicamente dependendo do OS."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def exibir_cabecalho(titulo: str):
        print("=" * 60)
        print(f"{titulo.center(60)}")
        print("=" * 60)

    @staticmethod
    def exibir_menu_principal() -> str:
        Menu.exibir_cabecalho("FASTDELIVERY EXPRESS - PAINEL OPERACIONAL")
        print(" [1] Cadastrar Novo Cliente")
        print(" [2] Listar Todos os Clientes")
        print(" [3] Buscar Cliente por CPF")
        print(" [4] Registrar Novo Pedido / Calcular Frete")
        print(" [5] Listar Todos os Pedidos Ativos")
        print(" [6] Atualizar Status de uma Entrega")
        print(" [0] Sair do Sistema")
        print("=" * 60)
        return input("Selecione uma operação: ")