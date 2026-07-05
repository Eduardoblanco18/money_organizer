import os
from modelos.Orcamento import Orcamento
from datetime import datetime

def menu_estatisticas(orcamento):
    while True:
        limpar_tela()
        print("""
    Menu de estátisticas:
    
    1- Maior gasto
    
    2- Menor gasto
    
    3- Média dos gastos
    
    4- Categoria com maior gasto
    
    5- Categoria com menor gasto

    6- Quantidade de gastos          

    7- Sair""")
        opcao = int(input(">"))
        
        limpar_tela()
        match opcao:
            case 1:
                print(orcamento.maior_gasto)
            case 2:
                print(orcamento.menor_gasto)
            case 3:
                print(f"Média total dos seus gastos: {orcamento.media_gastos}\n")
            case 4:
                print(orcamento.categoria_com_maior_gasto)
            case 5:
                print(orcamento.categoria_com_menor_gasto)
            case 6:
                print(f"Quantidade de gastos: {orcamento.quantidade_gastos}\n")
            case 7:
                print("Saindo da aba de estatísticas\n")
                return
        apertar_para_continuar()

def escolher_data(str=""):
    while True:
        data_str = input(f"Escreva a data {str} (dd/mm/aaaa)\n>")

        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            return data
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

def menu_historico(orcamento):
    if len(orcamento.gastos):
        print(orcamento.listar_historico())

        filtro = input("\n\ndeseja adicionar algum filtro? s/n\n>")

        if filtro.lower() == "s":
            limpar_tela()
            print("""
Qual tipo de filtro?
1- Descrição
2- Categoria
3- Data específica
4- Período
""")    
            while True:
                try:
                    tipo_de_filtro = int(input(">"))
                    break
                except ValueError:
                    print("Valor não reconhecível!")

            limpar_tela()
            match tipo_de_filtro:
                case 1:
                    descricao = input("Escreva o nome que procura\n>")
                    print(orcamento.buscar_gasto_por_descricao(descricao))
                case 2:
                    categoria = escolher_categoria()
                    print(orcamento.buscar_gasto_por_categoria(categoria))
                case 3:
                    data = escolher_data()
                    print(orcamento.buscar_gasto_por_data(data))
                case 4:
                    data_inicio = escolher_data("de início")
                    data_fim = escolher_data("de fim")
                    print(orcamento.buscar_gasto_por_perioso(data_inicio, data_fim))
    else:
        print("Historico vazio")


def escrever_salario():
    while True:
        try:
            salario = float(input("Qual é o seu salário?"))
            break
        except ValueError:
            print("Valor inválido")
    
    return salario

def menu_editar_salario(orcamento):
    limpar_tela()
    novo_salario = escrever_salario()

    certeza = input("Tem certeza que deseja trocar? s/n\n>").lower()

    if certeza == "s":
        orcamento.alterar_salario(novo_salario)
        orcamento.salvar_salario()
        print("Troca realizada com sucesso")
    else:
        print("Alteração cancelada")

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
    while True:
        try:
            valor = float(input("Quanto você gastou?\n>"))
            return valor
        
        except ValueError:
            print("Valor inválido!")

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
        print(f'{"Nº":<3} {"Descrição":<15} {"Categoria":<20} {"Valor"}')
        print("-"*50)
        for indice, gasto in enumerate(orcamento.gastos):
            print(f"{indice + 1:<3} {gasto.descricao:<15}{gasto.categoria:<20}{gasto.valor}")

        while True:
            try:
                posicao = int(input("Escolha um item que queira editar\n>")) - 1
                if 0 <= posicao < len(orcamento.gastos):
                    break
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
                orcamento.listar_orcamento()
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

def main():
    limpar_tela()

    salario = Orcamento.carregar_salario()

    if salario is None:
        salario = escrever_salario()

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