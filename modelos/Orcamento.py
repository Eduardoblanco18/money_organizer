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
        return (categoria[0], self.total_por_categoria(categoria[0]))
    
    @property
    def categoria_com_menor_gasto(self):
        categoria = min(
                        self.categorias,
                        key=lambda categoria: self.total_por_categoria(categoria[0]))
        return (categoria[0], self.total_por_categoria(categoria[0]))
    
    def listar_orcamento(self):
        return (            
f"""Salário: R${self.salario:.2f}

Necessidades: R${self.necessidade:.2f}

Lazer: R${self.lazer:.2f}

Investimentos: R${self.investimentos:.2f}

""")
    
    def total_por_categoria(self, categoria):
        return sum(gasto.valor 
                for gasto in self._gastos
                if gasto.categoria == categoria
                )
    
    def adicionar_gasto(self, descricao, categoria, valor):
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def adicionar_gasto_objeto(self, gasto):
        self._gastos.append(gasto)

    def excluir_gasto(self, posicao):
        del(self._gastos[posicao])

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

    def alterar_salario(self, novo_salario):
        self._salario = novo_salario

    def buscar_gasto_por_descricao(self, descricao):
        return self._filtrar(lambda gasto: descricao.title() in gasto.descricao.title())
    
    def buscar_gasto_por_categoria(self, categoria):
        return self._filtrar(lambda gasto: gasto.categoria == categoria)
                
    def buscar_gasto_por_data(self, data):
        return self._filtrar(lambda gasto: gasto.data == data)
    
    def buscar_gasto_por_periodo(self, data_inicio, data_fim):
        return self._filtrar(lambda gasto: data_inicio <= gasto.data <= data_fim)      
    
    def _filtrar(self, condicao):
        return [
            gasto
            for gasto in self._gastos
            if condicao(gasto)
        ]
    