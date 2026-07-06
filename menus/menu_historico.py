from utils import limpar_tela
from utils import escolher_categoria
from utils import escolher_data
from tabelamento import mostrar_gastos
from modelos.Orcamento import Orcamento

def menu_historico(orcamento:Orcamento)->None:
    if not orcamento.gastos:
        print("Historico vazio")
        return
    
    mostrar_gastos(orcamento.gastos)

    filtro = input("\n\ndeseja adicionar algum filtro? s/n\n>")

    if filtro.lower() == "s":
        aplicar_filtro(orcamento)
        

def aplicar_filtro(orcamento:Orcamento)->None:
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
            gastos = orcamento.buscar_gasto_por_descricao(input("Escreva o nome que procura\n>"))
        case 2:
            gastos = orcamento.buscar_gasto_por_categoria(escolher_categoria())
        case 3:
            gastos = orcamento.buscar_gasto_por_data(escolher_data())
        case 4:
            gastos = orcamento.buscar_gasto_por_periodo(escolher_data("de início"),escolher_data("de fim"))
        case _:
            print("Esse filtro não existe")
            return
            
    mostrar_gastos(gastos)