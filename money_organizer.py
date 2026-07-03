import os
import csv

gastos =[]

def ler_historico():
    gastos_antigos =[]

    with open("gastos.csv","r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for conteudo in leitor:
            conteudo["Valor"] = float(conteudo["Valor"])
            gastos.append(conteudo)

def salvar_gastos():
    with open("gastos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor"])
        
        escritor.writeheader()

        for gasto in gastos:
            escritor.writerow(gasto)

def gerar_relatorio(orcamento):
    texto = ""
    texto += f"Salário: R${round(orcamento["Salário"],2)}\n"
    for categoria in orcamento:
        if categoria == "Salário":
            continue
        gasto = calcular_gasto(categoria)
        resto = orcamento[categoria] - gasto

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

def calcular_gasto(categoria):
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

def fazer_relatorio(orcamento):
    limpar_tela()

    print(gerar_relatorio(orcamento))

    with open("Relátorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_relatorio(orcamento))

    apertar_para_continuar()

def listar_orcamento(orcamento):
    limpar_tela()
    for categoria in orcamento:
        print(f"{categoria}: R${round(orcamento[categoria],2)}\n")
    
    apertar_para_continuar()

def adicionar_gastos():
    limpar_tela()
    descricao = input("Com o que vc gastou?")

    escolha_certa = False
    while not escolha_certa:
        print("""
Qual categoria ele se encaixa?
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

    valor_valido = False
    while not valor_valido:
        try:
            valor = float(input("Quanto você gastou?\n\n"))
            valor_valido = True
        except ValueError:
            print("Valor inválido!")

    gastos.append({"Descrição": descricao, "Categoria": categoria, "Valor": valor})

    print("Gasto adicionado com sucesso\n")
    apertar_para_continuar()

def escolher_opcao(orcamento):
    print("""
    LISTA DE OPÇÔES
           
    1- Ver Orçamento
           
    2- Adicionar gastos
           
    3- Fazer relatório
           
    4- Sair
          
    """)
    try:
        escolha = int(input("Escolha uma opção\n>"))

        match escolha:
            case 1:
                listar_orcamento(orcamento)
                sair = False
            case 2:
                adicionar_gastos()
                sair = False
            case 3:
                fazer_relatorio(orcamento)
                sair = False
            case 4:
                salvar_gastos()
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
    salario_valido = False
    while not salario_valido:
        try:
            salario = float(input("Qual é o seu salário?"))
            salario_valido = True
        except ValueError:
            print("Valor inválido")

    orcamento = organizar_orcamento(salario)

    gastos = ler_historico()

    sair = False

    while not sair:
        sair = escolher_opcao(orcamento)
        limpar_tela()

if __name__ == "__main__":
    main()