from modelos.Orcamento import Orcamento
from modelos.Repositorio import RepositorioCSV
from utils import limpar_tela
from utils import escrever_valor
from menus.menu_principal import escolher_opcao


def main():
    limpar_tela()

    repositorio = RepositorioCSV()

    salario = repositorio.carregar_salario()

    if salario is None:
        salario = escrever_valor("Qual o seu salário?\n>")

        orcamento = Orcamento(salario)
        repositorio.salvar_salario(salario)
    else:
        orcamento = Orcamento(salario)

    for gasto in repositorio.carregar_gastos():
        orcamento.adicionar_gasto_objeto(gasto)

    sair = False

    while not sair:
        limpar_tela()
        sair = escolher_opcao(orcamento, repositorio)

if __name__ == "__main__":
    main()