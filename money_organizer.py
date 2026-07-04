import os
import csv

def excluir_gasto_da_lista(gastos, posicao):
    certeza = input("Tem certeza que deseja apagar (s/n)\n>")
    if certeza.lower() == "s":
        del(gastos[posicao])

def escolher_categoria():
    escolha_certa = False
    while not escolha_certa:
        print(
"""Qual categoria ele se encaixa?
1- Necessidade
2- Lazer
3- Investimentos""")
        try:
            opcao = int(input(">"))
            match opcao:
                case 1:
                    categoria = "Necessidade"
                    escolha_certa = True
                case 2:
                    categoria = "Lazer"
                    escolha_certa = True
                case 3:
                    categoria = "Investimentos"
                    escolha_certa = True
                case _:
                    print("Não existe essa opção")
        except ValueError:
            print("Não existe essa opção")

    return categoria

def editar_gasto(gastos, Detalhe, posicao):
    limpar_tela()
    edicao_fazivel = False
    while not edicao_fazivel:
        try:
            edicao_fazivel = True
            if Detalhe == "Descrição":
                edicao = input("Coloque o novo nome\n>")
            elif Detalhe == "Categoria":
                edicao = escolher_categoria()
            else:
                edicao = float(input("Coloque o novo valor\n>"))
        except ValueError:
            edicao_fazivel = False
            print("Não é possível realizar a edição")
    
    gastos[posicao][Detalhe] = edicao

def editar_historico(gastos):
    limpar_tela()
    print(f"{"Nº":<3} {"Descrição":<15}{"Categoria":<20}{"Valor"}")
    print("-"*50)
    for indice, gasto in enumerate(gastos):
        print(f"{indice + 1:<3} {gasto["Descrição"]:<15}{gasto["Categoria"]:<20}{gasto["Valor"]}")

    posicao_valida = False
    while not posicao_valida:
        try:
            posicao = int(input("Escolha um item que queira editar\n>")) - 1
            if 0 <= posicao < len(gastos):
                posicao_valida = True
            else:
                print("Valor incompatível!")
        except ValueError:
            print("Valor incompatível!")
    limpar_tela()
    print("""
O que deseja editar?
1- Trocar Nome
2- Trocar Categoria
3- Trocar Valor
4- Excluir
""")
    
    opcao_acessivel = False
    while not opcao_acessivel:
        try:
            opcao_escolhida = int(input(">"))
            opcao_acessivel = True
            match opcao_escolhida:
                case 1:
                    editar_gasto(gastos, "Descrição", posicao)
                case 2:
                    editar_gasto(gastos, "Categoria", posicao)
                case 3:
                    editar_gasto(gastos, "Valor", posicao)
                case 4:
                    excluir_gasto_da_lista(gastos, posicao)
                case _:
                    print("Opção Inválida")
                    opcao_acessivel = False
        except ValueError:
            print("Opção Inválida")


    apertar_para_continuar()

def vizualizar_historico(gastos):
    limpar_tela()
    print("-"*20)
    for indice,gasto in enumerate(gastos):
        print(f"{indice + 1}")
        for chave, valor in gasto.items():
            print(f"{chave}: {valor}")
        print("-"*20)
    
    apertar_para_continuar()

def ler_historico(gastos):
    with open("gastos.csv","r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for conteudo in leitor:
            conteudo["Valor"] = float(conteudo["Valor"])
            gastos.append(conteudo)

def salvar_gastos(gastos):
    with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor"])
        
        escritor.writeheader()

        for gasto in gastos:
            escritor.writerow(gasto)

def gerar_relatorio(orcamento,gastos):
    texto = ""
    texto += f"Salário: R${round(orcamento["Salário"],2)}\n"
    for categoria, limite in orcamento.items():
        if categoria == "Salário":
            continue
        gasto = calcular_gasto(categoria,gastos)
        resto = limite - gasto

        texto += (f"""
Categoria: {categoria}
    Limite: R${round(orcamento[categoria],2)}
    Gastos: R${round(gasto,2)}
    Resto:  R${round(resto,2)}
""")
    
    return texto

def limpar_tela():
    os.system("cls")

def apertar_para_continuar():
    input("aperte para continuar")

def calcular_gasto(categoria,gastos):
    return sum(gasto["Valor"] 
               for gasto in gastos
               if gasto["Categoria"] == categoria
               )

def organizar_orcamento(salario):
        necessidade = salario*0.5
        lazer = salario*0.3
        investimento = salario*0.2
        
        print("Organização feita!")
        apertar_para_continuar()
        limpar_tela()

        return {"Salário": salario,
                "Necessidade": necessidade,
                "Lazer": lazer,
                "Investimentos": investimento}

def fazer_relatorio(orcamento, gastos):
    limpar_tela()

    print(gerar_relatorio(orcamento, gastos))

    with open("Relátorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_relatorio(orcamento))

    apertar_para_continuar()

def listar_orcamento(orcamento):
    limpar_tela()
    for categoria in orcamento:
        print(f"{categoria}: R${round(orcamento[categoria],2)}\n")
    
    apertar_para_continuar()

def adicionar_gastos(gastos):
    limpar_tela()
    descricao = input("Com o que vc gastou?\n")

    categoria = escolher_categoria()

    valor_valido = False
    while not valor_valido:
        try:
            valor = float(input("Quanto você gastou?\n"))
            valor_valido = True
        except ValueError:
            print("Valor inválido!")

    gastos.append({"Descrição": descricao, "Categoria": categoria, "Valor": valor})

    print("\nGasto adicionado com sucesso\n")
    apertar_para_continuar()

def escolher_opcao(orcamento,gastos):
    print("""
    LISTA DE OPÇÔES
           
    1- Ver Orçamento
           
    2- Adicionar Gastos
           
    3- Fazer Relatório
          
    4- Ver Histórico de Gastos
          
    5- Editar Lista de Gastos
           
    6- Sair
          
    """)
    try:
        escolha = int(input("Escolha uma opção\n>"))

        match escolha:
            case 1:
                listar_orcamento(orcamento)
                sair = False
            case 2:
                adicionar_gastos(gastos)
                sair = False
            case 3:
                fazer_relatorio(orcamento, gastos)
                sair = False
            case 4:
                vizualizar_historico(gastos)
                sair = False
            case 5:
                editar_historico(gastos)
                sair = False
            case 6:
                salvar_gastos(gastos)
                sair = True
            case _:
                print("valor não reconhecido")
                apertar_para_continuar()
                sair = False
    except ValueError:
        print("valor não reconhecido")
        apertar_para_continuar()
        sair = False

    return sair

def main():
    gastos=[]
    salario_valido = False
    while not salario_valido:
        try:
            salario = float(input("Qual é o seu salário?"))
            salario_valido = True
        except ValueError:
            print("Valor inválido")

    orcamento = organizar_orcamento(salario)

    ler_historico(gastos)

    sair = False

    while not sair:
        sair = escolher_opcao(orcamento,gastos)
        limpar_tela()

if __name__ == "__main__":
    main()