from datetime import date
from typing import Any

class Gasto:
    def __init__(self, descricao:str, categoria:str, valor:float, data: date|None =None):
        self._descricao = descricao
        self._categoria = categoria
        self._valor = valor
        self._data = data if data else date.today()

    def __str__(self):
        return (
            f"Descrição: {self.descricao}\n"
            f"Categoria: {self.categoria}\n"
            f"Valor: {self.valor:.2f}\n"
            f"Data: {self.data.strftime("%d/%m/%Y")}\n"
            f"{"-"*20}"
        )

    @property
    def descricao(self)->str:
        return self._descricao

    @property
    def categoria(self)->str:
        return self._categoria

    @property
    def valor(self)->float:
        return self._valor
    
    @property
    def data(self)->date:
        return self._data
    
    def editar_descricao(self, descricao_nova:str)->None:
        self._descricao = descricao_nova

    def editar_categoria(self, categoria_nova:str)->None:
        self._categoria = categoria_nova

    def editar_valor(self, valor_novo:float)->None:
        self._valor = valor_novo

    def para_dict(self)->dict[str,Any]:
        return {
            "Descrição": self.descricao,
            "Categoria": self.categoria,
            "Valor": self.valor,
            "Data": self.data
        }