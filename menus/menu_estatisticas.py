from utils import limpar_tela
from utils import apertar_para_continuar

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