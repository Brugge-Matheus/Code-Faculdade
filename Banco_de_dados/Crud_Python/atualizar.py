import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"

# Conecta o usuário ao banco de dados através das informações passadas
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def atualizarDados():
    vUpd = input("Qual coluna vai receber os dados atualizados? >>> ")
    vAntigo = input("Qual o item que você quer mudar? >>> ")
    vAtual = input("Qual o item atualizado? >>> ")

    # Corrigindo a query para usar placeholders
    cmd = "UPDATE SALADEAULA SET {} = %s WHERE {} = %s;".format(vUpd, vAntigo)

    # Executando a query com os valores passados como parâmetros
    cursor.execute(cmd, (vAtual, vAntigo))
    conector.commit()

atualizarDados()
