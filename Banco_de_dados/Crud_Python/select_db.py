import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"


conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def ProcurarDados():
    colunaSelect = input("Qual a coluna desta tabela para selecionar? >>> ")
    query = "SELECT {} FROM SALADEAULA".format(colunaSelect)
    
    cursor.execute(query)
    myresult = cursor.fetchall()

    results = [list(map(str, item)) for item in myresult]
    alist = [x[0] for x in results]

    print(alist)
    
    
    conector.close()

ProcurarDados()
