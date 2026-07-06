from pathlib import Path
import csv
from datetime import datetime
from modelos.Gasto import Gasto

class RepositorioCSV:
    def __init__(self):
        self._pasta = Path("dados")
        self._pasta.mkdir(exist_ok=True)

        self._arquivo_gastos = self._pasta / "gastos.csv"
        self._arquivo_salario = self._pasta / "salario.csv"
        self._arquivo_relatorio = self._pasta / "relatório.txt"

    def salvar_salario(self, salario:float)->None:
        with open(self._arquivo_salario,"w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow([salario])
    
    def salvar_gastos(self, gastos:list[Gasto])->None:
        with open(self._arquivo_gastos, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["Descrição", "Categoria", "Valor", "Data"])
        
            escritor.writeheader()

            for gasto in gastos:
                escritor.writerow(gasto.para_dict())
    
    def carregar_salario(self)->float|None:
        try:
            with open(self._arquivo_salario,"r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                
                for linha in leitor:
                    return float(linha[0])
        
        except (FileNotFoundError,ValueError):
            return None

        return None

    def carregar_gastos(self)->list[Gasto]:
        gastos = []

        try:
            with open(self._arquivo_gastos,"r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)

                for conteudo in leitor:
                    data = datetime.strptime(conteudo["Data"], "%Y-%m-%d").date()

                    gasto = Gasto(
                        conteudo["Descrição"],
                        conteudo["Categoria"],
                        float(conteudo["Valor"]),
                        data
                    )
                    gastos.append(gasto)
        except (FileNotFoundError,ValueError):
            pass

        return gastos
    
    def salvar_relatorio(self, texto:str)->None:
        with open(self._arquivo_relatorio, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)