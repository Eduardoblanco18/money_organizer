class Gasto:
    def __init__(self, descricao, categoria, valor):
        self._descricao = descricao
        self._categoria = categoria
        self._valor = valor

    @property
    def descricao(self):
        return self._descricao

    @property
    def categoria(self):
        return self._categoria

    @property
    def valor(self):
        return self._valor
    
    def editar_descricao(self, descricao_nova):
        self._descricao = descricao_nova

    def editar_categoria(self, categoria_nova):
        self._categoria = categoria_nova

    def editar_valor(self, valor_novo):
        self._Valor = valor_novo

    def para_dict(self):
        return {
            "Descrição": self.descricao,
            "Categoria": self.categoria,
            "Valor": self.valor
        }