from utils import limpar_tela
from utils import escolher_categoria
from utils import escrever_valor
from tabelamento import mostrar_gastos

def editar_historico(orcamento):
    limpar_tela()
    if orcamento.gastos:
        mostrar_gastos(orcamento.gastos)

        while True:
            try:
                posicao = int(input("Escolha um item que queira editar\n>")) - 1
                if 0 <= posicao < orcamento.quantidade_gastos:
                    break
                else:
                    print("Valor incompatível!")
            except ValueError:
                print("Valor incompatível!")
        limpar_tela()
        print("O que deseja editar?\n1- Trocar Nome\n2- Trocar Categoria\n3- Trocar Valor\n4- Excluir\n5-Cancelar")
        
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
                    case 5:
                        print("Edição cancelada")    
                    case _:
                        print("Opção Inválida")
                        opcao_acessivel = False
            except ValueError:
                print("Opção Inválida")
    else:
        print("histórico vazio\n")

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
            edicao = escrever_valor("Quanto você gastou?\n>")
            gasto.editar_valor(edicao)