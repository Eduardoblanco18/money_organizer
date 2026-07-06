from modelos.Orcamento import Orcamento
from utils import limpar_tela
from utils import escrever_valor
from menus.menu_principal import escolher_opcao


def main():
    limpar_tela()

    salario = Orcamento.carregar_salario()

    if salario is None:
        salario = escrever_valor("Qual o seu salário?\n>")

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