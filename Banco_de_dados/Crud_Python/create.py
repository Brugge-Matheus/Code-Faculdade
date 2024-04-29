import mysql.connector

host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"

connector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = connector.cursor()

def inserirTabela():
    tabela = ""
    add = "s"
    var = 0
    while tabela != "0":
        nomeDaTabela = input("qual o nome da tabela que você quer criar? >>> ")
        
        while add == "s":
            add = input("voce deseja adicionar uma variavel? (s/n) >>> ")
            if add == "s":
                var += 1
                variavelnome = input("digite o nome da " + str(var) + "a variavel >>> ")
                variaveltipo = input("digite o tipo da " + str(var) + "a variavel >>> ")
                cursor.execute("ALTER TABLE " + nomeDaTabela + " ADD " + variavelnome + " " + variaveltipo + ";")
        if add == "n" or add == "N":
            tabela = "0"
            break 

inserirTabela()