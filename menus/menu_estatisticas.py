from utils import limpar_tela
from utils import apertar_para_continuar
from modelos.Orcamento import Orcamento

def menu_estatisticas(orcamento:Orcamento)->None:
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
                categoria, valor = orcamento.categoria_com_maior_gasto
                print(f"A categoria com maior gasto é {categoria} com o total de R${valor:.2f}")
            case 5:
                categoria, valor = orcamento.categoria_com_menor_gasto
                print(f"A categoria com menor gasto é {categoria} com o total de R${valor:.2f}")
            case 6:
                print(f"Quantidade de gastos: {orcamento.quantidade_gastos}\n")
            case 7:
                print("Saindo da aba de estatísticas\n")
                return
        apertar_para_continuar()