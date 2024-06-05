# Trabalho feito por Ana Babiak, Danieli, Stela, Douglas Wilhan, Leonardo Santana e Matheus Brugge
import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"


conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()


def main_menu():
    print("Escolha uma opção:")
    print("1. Cadastrar/modificar informações")
    print("2. Relatórios")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        cadastrar_modificar()
    elif escolha == '2':
        relatorios()
    elif escolha == '3':
        sair()
    else:
        print("Opção inválida. Tente novamente.")
        main_menu()

def cadastrar_modificar():
    print("\nPreencha as informações de cadastro do produto")
    nome = input("Digite o nome do produto? >>> ")
    descricao = input("Digite a descrição sobre o produto? >>> ")
    preco = input("Digite o preco do produto? >>> ")
    preco_de_custo = input("Digite o preço de custo do produto? >>> ")
    quantidade_estoque = input("Digite a quantidade em estoque do produto? >>> ")

    
    cmd = "INSERT INTO produtos (id, nome, descricao, preco, preco_de_custo,quantidade_estoque) VALUES (DEFAULT, %s, %s, %s, %s, %s)"
    valores = (nome, descricao, preco, preco_de_custo, quantidade_estoque)

    cursor.execute(cmd, valores)
    conector.commit()

    if cursor.rowcount > 0:
        print("\nConsulta executada com sucesso.")
    else:
        print("\nNenhuma linha afetada.")
        

def relatorios():
    print("\nEscolha o tipo de relatório que deseja")
    print("\n1. Listar todos os produtos >>> ")
    print("2. Contagem de produtos >>> ")
    print("3. Listagem detalhada")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        listagemGeral()
    elif escolha == '2':
        listagemContagem()
    elif escolha == '3':
        listagemDetalhada()
    else:
        print("Opção inválida. Tente novamente.")
        main_menu()
    
def listagemGeral():
    cursor.execute("SELECT nome,descricao,preco,preco_de_custo,quantidade_estoque FROM produtos")

    myresult = cursor.fetchall()

    for x in myresult:
        print(f"\n{x}")

def listagemContagem():
    cursor.execute("SELECT count(nome) from produtos")

    myresult = cursor.fetchone()

    print(f"\n{myresult[0]} Produtos encontrados")


def listagemDetalhada():
    coluna = input("Digite qual coluna deseja buscar >>> ")
    colunaCriterio = input("Digite qual coluna quer usar como critério na busca >>> ")
    operador = input("Digite o operador que deseja utilizar como criterio (ex: =, >, <, LIKE) >>> ")
    criterioFinal = input("Digite qual o criterio final que precisa ser validado >>> ")

    colunas_validas = ["id","nome", "descricao", "preco", "preco_de_custo", "quantidade_estoque"]
    if coluna not in colunas_validas or colunaCriterio not in colunas_validas:
        print("Coluna inválida.")
        return

    cmd = f"SELECT {coluna} FROM produtos WHERE {colunaCriterio} {operador} %s"
    valores = (criterioFinal,)

    cursor.execute(cmd, valores)
    myresult = cursor.fetchall()

    for x in myresult:
        print(f"\n{x}")


def sair():
    print("Você escolheu sair. Até logo!")
    

if __name__ == "__main__":
    main_menu()
