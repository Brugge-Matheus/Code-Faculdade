import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"


conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def inserirDados():
    varName = input("Qual o nome do aluno? >>> ")
    varCurso = input("Qual o curso do aluno? >>> ")

    
    cmd = "INSERT INTO SALADEAULA (NOME, CURSO) VALUES (%s, %s)"
    valores = (varName, varCurso)

    cursor.execute(cmd, valores)
    conector.commit()


inserirDados()

# Fecha a conexão
cursor.close()
conector.close()
