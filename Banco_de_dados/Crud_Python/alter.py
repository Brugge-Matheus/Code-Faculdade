import mysql.connector

# Coleta as informações para se conectar no banco de dados
host = "167.99.252.245"
user = "ESW2024_E13"
passwd = "AmigosDaFloresta"
database = "ESW2024_E13"

# Conecta o usuário ao banco de dados através das informações passadas
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

# Definindo uma função para inserir dados
def inserirDados():
    varNome = input("Qual é o nome do aluno? >>> ")
    varCurso = input("Qual é o curso do aluno? >>> ")

    consulta = "INSERT INTO SALADEAULA (NOME, CURSO) VALUES (%s, %s)"
    
    cursor.execute(consulta, (varNome, varCurso))
    
    # Commit para salvar as alterações no banco de dados
    conector.commit()

# Chamando a função para inserir dados
inserirDados()

# Fechando o cursor e a conexão
cursor.close()
conector.close()
