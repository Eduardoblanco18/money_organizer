from tabulate import tabulate

def mostrar_gastos(gastos):
    dados = []

    for indice, gasto in enumerate(gastos, start=1):
        dados.append([
            indice,
            gasto.descricao,
            gasto.categoria,
            gasto.valor,
            gasto.data.strftime("%d/%m/%Y")
        ])

    print(tabulate(dados, headers=["Nº", "Descrição", "Categoria", "Valor", "Data"], tablefmt="grid"))