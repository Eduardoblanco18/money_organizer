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
    def categorias(self):
        return [("Necessidade", self.necessidade), ("Lazer", self.lazer), ("Investimentos", self.investimentos)]
    
    @property
    def gastos(self):
        return self._gastos
    
    @property
    def gasto_totais(self):
        return sum(gasto.valor for gasto in self._gastos)
    
    @property
    def saldo(self):
        return self.salario - self.gasto_totais
    
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
                for gasto in self._gastos
                if gasto.categoria == categoria
                )
    
    def adicionar_gasto(self, descricao, categoria, valor):
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def excluir_gasto(self, posicao):
        del(self._gastos[posicao])

    def salvar_salario(self):
        with open("salario.csv","w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow([self.salario])
    
    def salvar_gastos(self):
        with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor", "Data"])
        
            escritor.writeheader()

            for gasto in self._gastos:
                escritor.writerow(gasto.para_dict())
    
    @staticmethod
    def carregar_salario():
        try:
            with open("salario.csv","r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                
                for linha in leitor:
                    return float(linha[0])
        
        except:
            return None

        return None

    def carregar_historico(self):
        self._gastos.clear()

        try:
            with open("gastos.csv","r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)

                for conteudo in leitor:
                    gasto = Gasto(
                        conteudo["Descrição"],
                        conteudo["Categoria"],
                        float(conteudo["Valor"]),
                        conteudo["Data"]
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
        texto = self.gerar_relatorio()
        
        print(texto)

        with open("Relatório.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

    def alterar_salario(self, novo_salario):
        self._salario = novo_salario
        self.salvar_salario()
    