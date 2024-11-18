import pandas as pd
from termcolor import colored
import os

def getDados(arquivo):
    ext = arquivo[-5:]
    if ext == '.xlsx':
        nome_arquivo = arquivo
    else:
        nome_arquivo = f"{arquivo}.xlsx"

    if os.path.exists(nome_arquivo):
        try:
            tabela = pd.read_excel(nome_arquivo)
            tabela["Email"]
            tabela["Nome"]

            return tabela
        except KeyError:
            print(colored("-----Erro-----\n|  Verifique se o nome das colunas\n|  estão escritas corretamente\n|  Email | Nome\n--------------", "red"))
            return False
        except Exception as err:
            print(colored(f"-----Erro-----\n|  Ocorreu um erro ao ler o arquivo: {err}\n--------------", "red"))
            return False
    else:
        print(colored(f"-----Erro-----\n|  Verifique se o caminho\n|  está correto ou se o arquivo existe\n|  você digitou: {arquivo}\n--------------", "red"))
        return False
