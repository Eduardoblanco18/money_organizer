import os
from modelos.Orcamento import Orcamento

def editar_gasto(orcamento, detalhe, posicao):
    gasto = orcamento.gastos[posicao]

    match detalhe:
        case "Descrição":
            edicao = input("Qual é o novo nome?\n>")
            gasto.editar_descricao(edicao)
        case "Categoria":
            edicao = escolher_categoria()
            gasto.editar_categoria(edicao)
        case "Valor":
            edicao = escrever_valor()
            gasto.editar_valor(edicao)


def escrever_valor():
    valor_valido = False
    while not valor_valido:
        try:
            valor = int(input("Quanto você gastou?\n>"))
            valor_valido = True 
        
        except ValueError:
            print("Valor inválido!")
    
    return valor

def selecionar_detalhes():
    descricao = input("Com o que você gastou?\n>")

    categoria = escolher_categoria()

    valor = escrever_valor()

    return descricao, categoria, valor

def escolher_categoria():
    escolha_certa = False
    while not escolha_certa:
        print(
"""Qual categoria ele se encaixa?
1- Necessidade
2- Lazer
3- Investimentos""")
        try:
            opcao = int(input(">"))
            match opcao:
                case 1:
                    categoria = "Necessidade"
                    escolha_certa = True
                case 2:
                    categoria = "Lazer"
                    escolha_certa = True
                case 3:
                    categoria = "Investimentos"
                    escolha_certa = True
                case _:
                    print("Não existe essa opção")
        except ValueError:
            print("Não existe essa opção")

    return categoria

def editar_historico(orcamento):
    limpar_tela()
    if len(orcamento.gastos):
        print(f"{"Nº":<3} {"Descrição":<15}{"Categoria":<20}{"Valor"}")
        print("-"*50)
        for indice, gasto in enumerate(orcamento.gastos):
            print(f"{indice + 1:<3} {gasto.descricao:<15}{gasto.categoria:<20}{gasto.valor}")

        posicao_valida = False
        while not posicao_valida:
            try:
                posicao = int(input("Escolha um item que queira editar\n>")) - 1
                if 0 <= posicao < len(orcamento.gastos):
                    posicao_valida = True
                else:
                    print("Valor incompatível!")
            except ValueError:
                print("Valor incompatível!")
        limpar_tela()
        print("O que deseja editar?\n1- Trocar Nome\n2- Trocar Categoria\n3- Trocar Valor\n4- Excluir")
        
        opcao_acessivel = False
        while not opcao_acessivel:
            try:
                opcao_escolhida = int(input(">"))
                opcao_acessivel = True
                match opcao_escolhida:
                    case 1:
                        editar_gasto(orcamento, "Descrição", posicao)
                    case 2:
                        editar_gasto(orcamento, "Categoria", posicao)
                    case 3:
                        editar_gasto(orcamento, "Valor", posicao)
                    case 4:
                        orcamento.excluir_gasto(posicao)
                    case _:
                        print("Opção Inválida")
                        opcao_acessivel = False
            except ValueError:
                print("Opção Inválida")
    else:
        print("histórico vazio\n")
    
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def apertar_para_continuar():
    input("aperte para continuar")

def escolher_opcao(orcamento):
    print(f"""
    LISTA DE OPÇÔES
          
    Salário: R${orcamento.salario:.2f}

    Gasto Totais: R${orcamento.gasto_totais:.2f}

    Saldo Restandte: R${orcamento.saldo:.2f}
           
    1- Ver Orçamento
           
    2- Adicionar Gastos
           
    3- Fazer Relatório
          
    4- Ver Histórico de Gastos
          
    5- Editar Lista de Gastos
           
    6- Sair
          
    """)
    try:
        escolha = int(input("Escolha uma opção\n>"))

        match escolha:
            case 1:
                limpar_tela()
                orcamento.listar_orcamento()
                apertar_para_continuar()
                sair = False
            case 2:
                limpar_tela()
                detalhes = selecionar_detalhes()
                orcamento.adicionar_gasto(*detalhes)
                apertar_para_continuar()
                sair = False
            case 3:
                limpar_tela()
                orcamento.escrever_relatorio()
                apertar_para_continuar()
                sair = False
            case 4:
                limpar_tela()
                orcamento.listar_historico()
                apertar_para_continuar()
                sair = False
            case 5:
                editar_historico(orcamento)
                apertar_para_continuar()
                sair = False
            case 6:
                orcamento.salvar_gastos()
                limpar_tela()
                sair = True
            case _:
                print("valor não reconhecido")
                apertar_para_continuar()
                sair = False
    except ValueError:
        print("valor não reconhecido")
        apertar_para_continuar()
        sair = False

    return sair

def main():
    limpar_tela()

    salario = Orcamento.carregar_salario()

    if salario == None:
        while True:
                try:
                    salario = float(input("Qual é o seu salário?"))
                    break
                except ValueError:
                    print("Valor inválido")

        orcamento = Orcamento(salario)
        orcamento.salvar_salario()
    else:
        orcamento = Orcamento(salario)

    orcamento.carregar_historico()

    sair = False

    while not sair:
        limpar_tela()
        sair = escolher_opcao(orcamento)

if __name__ == "__main__":
    main()