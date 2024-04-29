import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"

# Conecta o usuário ao banco de dados através das informações passadas
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()


def apagarTabela():
    varNome = input("Qual o nome da tabela que deseja apagar? >>> ")

    delete = "DROP TABLE {}".format(varNome)
    
    cursor.execute(delete)
    
    # Commit para salvar as alterações no banco de dados
    conector.commit()

apagarTabela()


cursor.close()
conector.close()

