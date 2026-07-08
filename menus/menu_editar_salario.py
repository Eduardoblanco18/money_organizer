from utils import limpar_tela
from utils import escrever_valor
from modelos.Orcamento import Orcamento
from modelos.Repositorio import RepositorioCSV

def menu_editar_salario(orcamento:Orcamento, repositorio:RepositorioCSV)->None:
    limpar_tela()
    novo_salario = escrever_valor("Qual é o seu salário?\n>")

    certeza = input("Tem certeza que deseja trocar? s/n\n>").lower()

    if certeza == "s":
        orcamento.alterar_salario(novo_salario)
        repositorio.salvar_salario(novo_salario)
        print("Troca realizada com sucesso")
    else:
        print("Alteração cancelada")