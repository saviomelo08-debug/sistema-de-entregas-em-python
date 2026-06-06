from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService
from util.menu import Menu
from util.formatador import Formatador
from util.validador import Validador

def main():
    cliente_service = ClienteService()
    pedido_service = PedidoService()

    # Massa de dados inicial mockada para fins de teste imediato
    try:
        c_mock = cliente_service.cadastrar_cliente("Carlos Drummond", "12345678901", "11988887777", "Av Paulista, 1000")
        pedido_service.criar_pedido("PED-001", c_mock, 3.5, 12.0, EntregaService.obter_tipo_entrega(2))
    except Exception:
        pass

    while True:
        Menu.limpar_tela()
        opcao = Menu.exibir_menu_principal()

        if opcao == "1":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("CADASTRO DE NOVO CLIENTE")
            nome = input("Nome Completo: ")
            cpf = input("CPF (apenas números): ")
            telefone = input("Telefone para Contato: ")
            endereco = input("Endereço de Entrega: ")

            if Validador.validar_vazio(nome) or Validador.validar_vazio(cpf):
                print("\n❌ Erro: Nome e CPF são campos obrigatórios.")
            elif not Validador.validar_cpf(cpf):
                print("\n❌ Erro: Formato de CPF inválido. Certifique-se de preencher 11 dígitos.")
            else:
                try:
                    cliente_service.cadastrar_cliente(nome, cpf, telefone, endereco)
                    print("\n✅ Cliente adicionado com sucesso à base de dados!")
                except ValueError as e:
                    print(f"\n❌ Erro Operacional: {e}")
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "2":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("CLIENTES REGISTRADOS")
            clientes = cliente_service.listar_clientes()
            if not clientes:
                print("Nenhum cliente cadastrado no momento.")
            for c in clientes:
                print(f"• Nome: {c.nome} | CPF: {Formatador.formatar_cpf(c.cpf)} | Contato: {c.telefone}")
                print(f"  Endereço: {c.endereco}\n" + "-"*60)
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "3":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("PESQUISAR CLIENTE")
            cpf = input("Informe o CPF do cliente procurado: ")
            cliente = cliente_service.buscar_por_cpf(cpf)
            if cliente:
                print(f"\n🔍 Registro Localizado:")
                print(f" Nome: {cliente.nome}")
                print(f" CPF: {Formatador.formatar_cpf(cliente.cpf)}")
                print(f" Telefone: {cliente.telefone}")
                print(f" Endereço: {cliente.endereco}")
            else:
                print("\n❌ Cliente não localizado no banco de dados.")
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "4":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("GERAR NOVO PEDIDO DE ENTREGA")
            cpf_cliente = input("Digite o CPF do cliente solicitante: ")
            cliente = cliente_service.buscar_por_cpf(cpf_cliente)

            if not cliente:
                print("\n❌ Erro: Cliente não localizado. Efetue o cadastro antes de criar pedidos.")
            else:
                codigo = input("Código Identificador do Pedido: ")
                try:
                    peso = float(input("Peso estimado da carga (kg): "))
                    distancia = float(input("Distância estimada da rota (km): "))
                    print("\nModalidades de Envio Disponíveis:")
                    print(" [1] Entrega Comum   (Fórmula: Km * R$ 1.50)")
                    print(" [2] Entrega Expressa (Fórmula: Km * R$ 3.00)")
                    print(" [3] Entrega Premium (Fórmula: Km * R$ 5.00 + R$ 20.00 fixa)")
                    tipo_opcao = int(input("Escolha a modalidade desejada: "))

                    tipo_entrega = EntregaService.obter_tipo_entrega(tipo_opcao)
                    pedido = pedido_service.criar_pedido(codigo, cliente, peso, distancia, tipo_entrega)

                    print(f"\n✅ Pedido '{pedido.codigo}' registrado e pronto para triagem!")
                    print(f"💰 Custo de Envio calculado via Polimorfismo: {Formatador.formatar_moeda(pedido.valor_frete)}")
                except ValueError as e:
                    print(f"\n❌ Erro de Entrada de Dados: {e}")
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "5":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("RELAÇÃO GERAL DE PEDIDOS")
            pedidos = pedido_service.listar_pedidos()
            if not pedidos:
                print("Nenhum pedido cadastrado no momento.")
            for p in pedidos:
                print(f"📦 ID: {p.codigo} | Destinatário: {p.cliente.nome}")
                print(f"   Frete: {Formatador.formatar_moeda(p.valor_frete)} | Status Atual: [{p.status}]")
                print("-" * 60)
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "6":
            Menu.limpar_tela()
            Menu.exibir_cabecalho("ATUALIZAÇÃO DE STATUS LOGÍSTICO")
            codigo = input("Código do Pedido: ")
            pedido = pedido_service.buscar_por_codigo(codigo)

            if not pedido:
                print("\n❌ Pedido não encontrado no sistema.")
            else:
                print(f"\nStatus Atual: {pedido.status}")
                print("\nSelecione o novo estágio:")
                print(" [1] Em preparação")
                print(" [2] Saiu para entrega")
                print(" [3] Entregue")
                print(" [4] Cancelado")
                st_opcao = input("Opção desejada: ")

                status_map = {
                    "1": "Em preparação",
                    "2": "Saiu para entrega",
                    "3": "Entregue",
                    "4": "Cancelado"
                }

                novo_status = status_map.get(st_opcao)
                if novo_status:
                    pedido_service.atualizar_status(codigo, novo_status)
                    print(f"\n✅ Transição de status efetuada para '{novo_status}' com sucesso!")
                else:
                    print("\n❌ Entrada Inválida. Nenhuma alteração foi realizada.")
            input("\nPressione [Enter] para retornar ao menu principal...")

        elif opcao == "0":
            print("\nEncerrando sessão... Obrigado por utilizar a FastDelivery Express!")
            break
        else:
            print("\n❌ Comando inválido. Tente novamente.")
            input("\nPressione [Enter] para continuar...")

if __name__ == "__main__":
    main()