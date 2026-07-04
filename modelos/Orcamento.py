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
    def salario(self):
        return self._salario
    
    @property
    def gastos(self):
        return self._gastos
    
    @property
    def categorias(self):
        return [("Necessidade", self.necessidade), ("Lazer", self.lazer), ("Investimentos", self.investimentos)]
    
    def listar_orcamento(self):
        print(            
f"""Salário: R${self.salario:.2f}

Necessidades: R${self.necessidade:.2f}

Lazer: R${self.lazer:.2f}

Investimentos: R${self.investimentos:.2f}

""")
        
    def listar_historico(self):
        print("-"*20)
        for indice,gasto in enumerate(self._gastos, start= 1):
            print(f"{indice}")
            print(gasto)
            print("-"*20)
    
    def total_por_categoria(self, categoria):
        return sum(gasto.valor 
                for gasto in self.gastos
                if gasto.categoria == categoria
                )
    
    def adicionar_gasto(self, descricao, categoria, valor):
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def excluir_gasto(self, posicao):
        del(self._gastos[posicao])
    
    def salvar_gastos(self):
        with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor"])
        
            escritor.writeheader()

            for gasto in self.gastos:
                escritor.writerow(gasto.para_dict())

    def carregar_historico(self):
        self._gastos.clear()

        try:
            with open("gastos.csv","r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)

                for conteudo in leitor:
                    gasto = Gasto(
                        conteudo["Descrição"],
                        conteudo["Categoria"],
                        float(conteudo["Valor"])
                    )
                    self._gastos.append(gasto)
        except FileNotFoundError:
            pass

    def gerar_relatorio(self):
        texto = ""
        texto += f"Salário: R${self.salario:.2f}\n"
        for categoria, limite in self.categorias:
            gasto = self.total_por_categoria(categoria)
            resto = limite - gasto

            texto += f"""
Categoria: {categoria}
    Limite: R${limite:.2f}
    Gasto: R${gasto:.2f}
    Resto: R${resto:.2f}
"""
        return texto
    
    def escrever_relatorio(self):
        print(self.gerar_relatorio())

        with open("Relatório.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(self.gerar_relatorio())
    