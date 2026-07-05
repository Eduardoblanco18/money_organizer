import os
import csv
from modelos.Gasto import Gasto
from datetime import datetime

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
    def total_gastos(self):
        return sum(gasto.valor for gasto in self._gastos)
    
    @property
    def saldo(self):
        return self.salario - self.total_gastos
    
    @property
    def quantidade_gastos(self):
        return len(self._gastos)
    
    @property
    def maior_gasto(self):
        if not self._gastos:
            return None
        return max(self._gastos, key=lambda gasto: gasto.valor)
    
    @property
    def menor_gasto(self):
        if not self._gastos:
            return None
        return min(self._gastos, key=lambda gasto: gasto.valor)
    
    @property
    def media_gastos(self):
        if not self._gastos:
            return 0
        return  self.total_gastos / self.quantidade_gastos 
    
    @property
    def categoria_com_maior_gasto(self):
        categoria = max(
                        self.categorias, 
                        key=lambda categoria: self.total_por_categoria(categoria[0]))
        return f"A categoria com maior gasto foi {categoria[0]} com um total de R${self.total_por_categoria(categoria[0]):.2f}\n"
    
    @property
    def categoria_com_menor_gasto(self):
        categoria = min(
                        self.categorias,
                        key=lambda categoria: self.total_por_categoria(categoria[0]))
        return f"A categoria com menor gasto foi {categoria[0]} com um total de R${self.total_por_categoria(categoria[0]):.2f}\n"
    
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
                    data = datetime.strptime(conteudo["Data"], "%Y-%m-%d").date()

                    gasto = Gasto(
                        conteudo["Descrição"],
                        conteudo["Categoria"],
                        float(conteudo["Valor"]),
                        data
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

    def buscar_gasto_por_descricao(self, descricao):
        print("-"*20)
        for indice, gasto in enumerate(self._gastos, start=1):
            if gasto.descricao.lower() == descricao.lower():
                print(indice)
                print(gasto)
                
    def buscar_gasto_por_categoria(self, categoria):
        print("-"*20)
        for indice, gasto in enumerate(self._gastos, start=1):
            if gasto.categoria == categoria.title():
                print(indice)
                print(gasto)
                
    def buscar_gasto_por_data(self, data):
        print("-"*20)
        for indice, gasto in enumerate(self._gastos, start=1):
            if gasto.data == data:
                print(indice)
                print(gasto)
    
    def buscar_gasto_por_perioso(self, data_inicio, data_fim):
        print("-"*20)
        for indice, gasto in enumerate(self._gastos, start=1):
            if data_inicio <= gasto.data <= data_fim:
                print(indice)
                print(gasto)
                
    