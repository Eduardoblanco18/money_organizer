import os

gastos =[]

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

        return {"Necessidade": necessidade,
                "Lazer": lazer,
                "Investimentos": investimento}

def fazer_relatorio(orcamento):
    os.system("cls")

    gastos_necessidade = calcular_gasto("Necessidade")
    
    gastos_lazer = calcular_gasto("Lazer")
    
    gastos_investimento = calcular_gasto("Investimentos")
    
    resto_necessidade = orcamento["Necessidade"] - gastos_necessidade
    resto_lazer = orcamento["Lazer"] - gastos_lazer
    resto_investimento = orcamento["Investimentos"] - gastos_investimento

    print(f"""

    Categoria: Necessidade
        Limite: R${round(orcamento["Necessidade"], 2)}
        Gasto: R${round(gastos_necessidade, 2)}
        Resto: R${round(resto_necessidade, 2)}

    Categoria: Lazer
        Limite: R${round(orcamento["Lazer"], 2)}
        Gasto: R${round(gastos_lazer, 2)}
        Resto: R${round(resto_lazer, 2)}

    Categoria: Investimento
        Limite: R${round(orcamento["Investimentos"], 2)}
        Gasto: R${round(gastos_investimento, 2)}
        Resto: R${round(resto_investimento, 2)}

    """)

    apertar_para_continuar()


def listar_orcamento(orcamento):
    os.system("cls")
    print(f"""
    Necessidade: R${round(orcamento["Necessidade"],2)}

    Lazer: R${round(orcamento["Lazer"], 2)}

    Investimentos: R${round(orcamento["Investimentos"], 2)}
    
    """)
    apertar_para_continuar()

def adicionar_gastos():
    os.system("cls")
    descricao = input("Com o que vc gastou?")

    escolha_certa = False
    while not escolha_certa:
        print("""
        Qual categoria ele se encaixa?
            1- Necessidade
            2- Lazer
            3- Investimentos
        """)
        opcao = int(input(">"))
        match opcao:
            case 1:
                categoria = "Necessidade"
                escolha_certa = not escolha_certa
            case 2:
                categoria = "Lazer"
                escolha_certa = not escolha_certa
            case 3:
                categoria = "Investimentos"
                escolha_certa = not escolha_certa 
            case _:
                print("Não existe essa opção")

    valor = int(input("Quanto você gastou?"))

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
     
    escolha = int(input("Escolha uma opção"))

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
            sair = True
        case _:
            print("valor não reconhecido")
            sair = False

    return sair

def main():
    salario = float(input("Qual é o seu salário?"))

    orcamento = organizar_orcamento(salario)

    sair = False

    while not sair:
        sair = escolher_opcao(orcamento)
        os.system("cls")

if __name__ == "__main__":
    main()