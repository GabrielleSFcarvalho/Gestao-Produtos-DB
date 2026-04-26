import mysql.connector
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='gestao_produtos'
)

cursor = conexao.cursor()

# CRUD
nome_produto = "Chá"
valor = 6
comando = f'DELETE FROM Vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()

# CREATE
#nome_produto = "Abacate"
#valor = 10.0
#comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()
#resultado = cursor.fetchall()

# READ
#comando = f'SELECT * FROM Vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

# UPDATE
#nome_produto = "Chá"
#valor = 6
#comando = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

# DELETE