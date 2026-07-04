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
    
    def adicionar_gasto(self, descricao, categoria, valor):
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def excluir_gasto(self, posicao):
        del(self._gastos[posicao])
    
    def calcular_gasto(self, categoria):
        return sum(gasto._valor 
                for gasto in self._gastos
                if gasto._categoria == categoria
                )
    
    def salvar_gastos(self):
        with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor"])
        
            escritor.writeheader()

            for gasto in self._gastos:
                escritor.writerow(gasto)

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
    