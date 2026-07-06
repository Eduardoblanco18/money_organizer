from utils import limpar_tela
from utils import apertar_para_continuar
from utils import escolher_categoria
from utils import escrever_valor
from menus.menu_editar_historico import editar_historico
from menus.menu_editar_salario import menu_editar_salario
from menus.menu_estatisticas import menu_estatisticas
from menus.menu_historico import menu_historico

def escolher_opcao(orcamento):
    print(f"""
    LISTA DE OPÇÔES
          
    Salário: R${orcamento.salario:.2f}

    Gasto Totais: R${orcamento.total_gastos:.2f}

    Saldo Restandte: R${orcamento.saldo:.2f}
           
    1- Ver Orçamento
           
    2- Adicionar Gastos
           
    3- Fazer Relatório
          
    4- Ver Histórico de Gastos
          
    5- Editar Lista de Gastos

    6- Alterar Salário
           
    7- Estátiscas
    
    8- Sair
          
    """)
    try:
        escolha = int(input("Escolha uma opção\n>"))

        match escolha:
            case 1:
                limpar_tela()
                print(orcamento.listar_orcamento())
            case 2:
                limpar_tela()
                detalhes = selecionar_detalhes()
                orcamento.adicionar_gasto(*detalhes)
            case 3:
                limpar_tela()
                print(orcamento.escrever_relatorio())
            case 4:
                limpar_tela()
                menu_historico(orcamento)
            case 5:
                editar_historico(orcamento)
            case 6:
                menu_editar_salario(orcamento)
            case 7:
                menu_estatisticas(orcamento)
            case 8:
                orcamento.salvar_gastos()
                limpar_tela()
                return True
            case _:
                print("valor não reconhecido")

    except ValueError:
        print("valor não reconhecido")
    
    apertar_para_continuar()

    return False

def selecionar_detalhes():
    descricao = input("Com o que você gastou?\n>")

    categoria = escolher_categoria()

    valor = escrever_valor("Quanto foi o valor gasto?\n>")

    return descricao, categoria, valor