import os
from datetime import datetime

def limpar_tela()->None:
    os.system("cls" if os.name == "nt" else "clear")

def apertar_para_continuar()->None:
    input("aperte para continuar")

def escrever_valor(texto:str = ">")->float:
    while True:
        try:
            valor = float(input(texto))
            return valor
        
        except ValueError:
            print("Valor inválido!")

def escolher_data(texto:str="")->datetime:
    while True:
        data_str = input(f"Escreva a data {texto} (dd/mm/aaaa)\n>")

        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            return data
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

def escolher_categoria()->str:
    categorias = {
        1:"Necessidade",
        2:"Lazer",
        3:"Investimentos"
    }
    while True:
        print(
"""Qual categoria ele se encaixa?
1- Necessidade
2- Lazer
3- Investimentos""")
        
        try:
            return categorias[int(input(">"))]
        except (ValueError, KeyError):
            print("Não existe essa opção!")