import os
from datetime import datetime

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

def escolher_data(str=""):
    while True:
        data_str = input(f"Escreva a data {str} (dd/mm/aaaa)\n>")

        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            return data
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

def escolher_categoria():
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