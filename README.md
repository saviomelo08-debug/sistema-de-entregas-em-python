# sistema-de-entregas-em-python
# FastDelivery Express - Sistema de Gerenciamento Logístico

O **FastDelivery Express** é um ecossistema desenvolvido em terminal voltado para o monitoramento logístico e gerenciamento operacional de entregas expressas e frotas urbanas comerciais.

## 🚀 Tecnologias Utilizadas
* **Python 3** (Funcionalidades avançadas de Orientação a Objetos)
* **Git** (Controle e histórico de versões do código fonte)
* **GitHub** (Hospedagem pública e colaboração)

---

## 📂 Arquitetura de Pastas e Componentes

A organização do código obedece fielmente ao princípio de separação de responsabilidades em camadas arquiteturais profissionais:



fast_delivery/
│
├── main.py                   # Ponto de inicialização do programa e loop do menu
├── modelos/                  # Armazena as entidades/classes principais de domínio
│   ├── pessoa.py             # Superclasse para encapsulamento de dados comuns
│   ├── cliente.py            # Entidade herdeira contendo os dados do cliente
│   ├── entregador.py         # Entidade herdeira com dados específicos do veículo
│   ├── pedido.py             # Agrupador do fluxo lógico do frete e seus status
│   └── entrega.py            # Estruturas filhas responsáveis por calcular o frete
│
├── interfaces/               # Contratos abstratos e desacoplamento
│   └── calculo_frete_interface.py
│
├── services/                 # Concentra as regras de negócio e persistência em memória
│   ├── pedido_service.py
│   ├── cliente_service.py
│   └── entrega_service.py
│
└── util/                     # Auxiliares técnicos (Formatações, menus e validações)
    ├── validador.py
    ├── menu.py
    └── formatador.py
