import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"


conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()
print("Seja bem vindo ao sistema de relatórios")

print("Selecione a opção desejada")
print("1. Cadastrar/modificar informações")
print("2. Relatórios")
print("3. sair")

def cadastrarInfo():
    print("Cadastrar informações")



def relatorios():
    print("sim")


def relProdutos():
    inicial = input("Data de inicio: ")
    final = input("Data de inicio: ")


def relPedidos():
    inicial = input("Data de inicio: ")
    final = input("Data de inicio: ")


def relDespesasOperacionais():
    inicial = input("Data de inicio: ")
    final = input("Data de inicio: ")