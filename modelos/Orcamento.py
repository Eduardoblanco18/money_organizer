from modelos.Gasto import Gasto
from datetime import date
from collections.abc import Callable

class Orcamento:
    def __init__(self, salario):
        self._gastos: list[Gasto] = []
        
        self._salario = salario
        
    @property
    def necessidade(self)->float: 
        return self._salario*0.5
    
    @property
    def lazer(self)->float:
        return self._salario*0.3

    @property
    def investimentos(self)->float:
        return self._salario*0.2
    
    @property
    def salario(self)->float:
        return self._salario
    
    @property
    def categorias(self)->list[tuple[str, float]]:
        return [("Necessidade", self.necessidade), ("Lazer", self.lazer), ("Investimentos", self.investimentos)]
    
    @property
    def gastos(self)->list[Gasto]:
        return self._gastos
    
    @property
    def total_gastos(self)->float:
        return sum(gasto.valor for gasto in self._gastos)
    
    @property
    def saldo(self)->float:
        return self.salario - self.total_gastos
    
    @property
    def quantidade_gastos(self)->int:
        return len(self._gastos)
    
    @property
    def maior_gasto(self)->Gasto|None:
        if not self.quantidade_gastos:
            return None
        return max(self._gastos, key=lambda gasto: gasto.valor)
    
    @property
    def menor_gasto(self)->Gasto|None:
        if not self.quantidade_gastos:
            return None
        return min(self._gastos, key=lambda gasto: gasto.valor)
    
    @property
    def media_gastos(self)->float:
        if not self.quantidade_gastos:
            return 0
        return  self.total_gastos / self.quantidade_gastos 
    
    @property
    def categoria_com_maior_gasto(self)->tuple[str, float]:
        categoria = max(
                        self.categorias, 
                        key=lambda categoria: self.total_por_categoria(categoria[0]))
        return (categoria[0], self.total_por_categoria(categoria[0]))
    
    @property
    def categoria_com_menor_gasto(self)->tuple[str, float]:
        categoria = min(
                        self.categorias,
                        key=lambda categoria: self.total_por_categoria(categoria[0]))
        return (categoria[0], self.total_por_categoria(categoria[0]))
    
    def listar_orcamento(self)->str:
        return (            
f"""Salário: R${self.salario:.2f}

Necessidades: R${self.necessidade:.2f}

Lazer: R${self.lazer:.2f}

Investimentos: R${self.investimentos:.2f}

""")
    
    def total_por_categoria(self, categoria:str)->float:
        return sum(gasto.valor 
                for gasto in self._gastos
                if gasto.categoria == categoria
                )
    
    def adicionar_gasto(self, descricao:str, categoria:str, valor:float)->None:
        gasto = Gasto(descricao, categoria, valor)

        self._gastos.append(gasto)

    def adicionar_gasto_objeto(self, gasto:Gasto)->None:
        self._gastos.append(gasto)

    def excluir_gasto(self, posicao:int)->None:
        del(self._gastos[posicao])

    def gerar_relatorio(self)->str:
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
    Porcentagem usada: {(self.total_por_categoria(categoria)/limite):.2%}
"""
            if resto < 0:
                texto+=f"""
    Você ultrapassou seu limite nesta categoria
    Você ultrapassou o limite por R${abs(resto):.2f}
"""
        return texto

    def alterar_salario(self, novo_salario:float)->None:
        self._salario = novo_salario

    def buscar_gasto_por_descricao(self, descricao:str)->list[Gasto]:
        return self._filtrar(lambda gasto: descricao.lower() in gasto.descricao.lower())
    
    def buscar_gasto_por_categoria(self, categoria:str)->list[Gasto]:
        return self._filtrar(lambda gasto: gasto.categoria == categoria)
                
    def buscar_gasto_por_data(self, data:date)->list[Gasto]:
        return self._filtrar(lambda gasto: gasto.data == data)
    
    def buscar_gasto_por_periodo(self, data_inicio:date, data_fim:date)->list[Gasto]:
        return self._filtrar(lambda gasto: data_inicio <= gasto.data <= data_fim)      
    
    def _filtrar(self, condicao:Callable[[Gasto],bool])->list[Gasto]:
        return [
            gasto
            for gasto in self._gastos
            if condicao(gasto)
        ]
    