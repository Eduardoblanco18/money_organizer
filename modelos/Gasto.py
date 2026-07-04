from datetime import date

class Gasto:
    def __init__(self, descricao, categoria, valor):
        self._descricao = descricao
        self._categoria = categoria
        self._valor = valor
        self._data = date.today().strftime("%d/%m/%Y")

    def __str__(self):
        return (
            f"Descrição: {self.descricao}\n"
            f"Categoria: {self.categoria}\n"
            f"Valor: {self.valor:.2f}\n"
            f"Data: {self._data}"

        )

    @property
    def descricao(self):
        return self._descricao

    @property
    def categoria(self):
        return self._categoria

    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        return self._data
    
    def editar_descricao(self, descricao_nova):
        self._descricao = descricao_nova

    def editar_categoria(self, categoria_nova):
        self._categoria = categoria_nova

    def editar_valor(self, valor_novo):
        self._valor = valor_novo

    def para_dict(self):
        return {
            "Descrição": self.descricao,
            "Categoria": self.categoria,
            "Valor": self.valor,
            "Data": self.data
        }