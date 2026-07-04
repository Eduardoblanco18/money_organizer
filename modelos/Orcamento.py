import os
import csv
from modelos.Gasto import Gasto

class Orcamento:
    def __init__(self, salario):
        self._gastos = []
        self._salario = salario
        
    @property
    def necessidade(self):
        return self._salario*0.5
    
    @property
    def lazer(self):
        return self._salario*0.3

    @property
    def investimentos(self):
        return self._salario*0.2
    
    @property
    def gastos(self):
        return self._gastos
    
    def limpar_tela(self):
        os.system("cls")
    
    def adicionar_gasto(self, descricao, categoria, valor):
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def excluir_gasto(self, posicao):
        del(self._gastos[posicao])
    
    def calcular_gasto(self, categoria):
        return sum(gasto.valor 
                for gasto in self._gastos
                if gasto.categoria == categoria
                )
    
    def salvar_gastos(self):
        with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor"])
        
            escritor.writeheader()

            for gasto in self._gastos:
                escritor.writerow(gasto.para_dict())

    def carregar_historico(self):
        with open("gastos.csv","r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for conteudo in leitor:
                gasto = Gasto(
                    conteudo["Descrição"],
                    conteudo["Categoria"],
                    float(conteudo["Valor"])
                )
                self._gastos.append(gasto)

    def menu_edicao(self):
        self.limpar_tela()
        print(f"{"Nº":<3} {"Descrição":<15}{"Categoria":<20}{"Valor"}")
        print("-"*50)
        for indice, gasto in enumerate(self._gastos):
            print(f"{indice + 1:<3} {gasto.descricao:<15}{gasto.categoria:<20}{gasto.valor}")

        posicao_valida = False
        while not posicao_valida:
            try:
                posicao = int(input("Escolha um item que queira editar\n>")) - 1
                if 0 <= posicao < len(self._gastos):
                    posicao_valida = True
                else:
                    print("Valor incompatível!")
            except ValueError:
                print("Valor incompatível!")
        self.limpar_tela()
        print("""
O que deseja editar?
1- Trocar Nome
2- Trocar Categoria
3- Trocar Valor
4- Excluir
""")
        
        opcao_acessivel = False
        while not opcao_acessivel:
            try:
                opcao_escolhida = int(input(">"))
                opcao_acessivel = True
                match opcao_escolhida:
                    case 1:
                        self.editar_gasto("Descrição", posicao)
                    case 2:
                        self.editar_gasto("Categoria", posicao)
                    case 3:
                        self.editar_gasto("Valor", posicao)
                    case 4:
                        self.excluir_gasto(posicao)
                    case _:
                        print("Opção Inválida")
                        opcao_acessivel = False
            except ValueError:
                print("Opção Inválida")

    def editar_gasto(self, detalhe, posicao):
        self.limpar_tela()
        gasto = self._gastos[posicao]
        edicao_fazivel = False
        while not edicao_fazivel:
            try:
                edicao_fazivel = True
                if detalhe == "Descrição":
                    edicao = input("Coloque o novo nome\n>")
                    gasto.editar_descricao(edicao)
                elif detalhe == "Categoria":
                    edicao = self.escolher_categoria()
                    gasto.editar_categoria(edicao)
                else:
                    edicao = float(input("Coloque o novo valor\n>"))
                    gasto.editar_valor(edicao)
            except ValueError:
                edicao_fazivel = False
                print("Não é possível realizar a edição")

    def escolher_categoria(self):
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
    