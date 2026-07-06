import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def apertar_para_continuar():
    input("aperte para continuar")

def escrever_valor(texto = ">"):
    while True:
        try:
            valor = float(input(texto))
            return valor
        
        except ValueError:
            print("Valor inválido!")