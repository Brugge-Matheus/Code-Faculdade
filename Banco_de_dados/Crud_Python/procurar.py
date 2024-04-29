import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"


conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def procurarDados():
    colunaSelect = input("Qual a coluna desta tabela para selecionar? >>> ")
    cursor.execute("SELECT " +colunaSelect+ " FROM SALADEAULA;")

    myresult = cursor.fetchall()

    results = [list(str(item) for item in t) for t in myresult]
    alist = []
    for x in results:
        alist.append(x)

    print(alist)
    conector.close()

procurarDados()