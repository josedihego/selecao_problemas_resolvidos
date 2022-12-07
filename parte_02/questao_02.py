import sqlite3

conexao = sqlite3.connect('contas.sqlite')

cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS CONTA")

comando_criacao = """ CREATE TABLE CONTA (
    ID INT PRIMARY KEY NOT NULL,
    CODIGO CHAR(5) NOT NULL,
    AGENCIA CHAR(10) NOT NULL,
    NUMERO CHAR(10) NOT NULL
) """

cursor.execute(comando_criacao)
conexao.commit()
conexao.close()

conexao = sqlite3.connect('contas.sqlite')
comando_insercao = """INSERT INTO CONTA (ID, CODIGO, AGENCIA, NUMERO) VALUES (:ID, :CODIGO, :AGENCIA, :NUMERO) ;"""

parametros = {
    'ID' : 1,
    'CODIGO': '001',
    'AGENCIA': '6789-9',
    'NUMERO' : '56789-99'
}

parametros2 = {
    'ID' : 2,
    'CODIGO': '002',
    'AGENCIA': '78789-01',
    'NUMERO' : '7631723-89'
}
conexao.execute(comando_insercao, parametros)
conexao.execute(comando_insercao, parametros2)
conexao.commit()
conexao.close()

conexao = sqlite3.connect('contas.sqlite')
cursor = conexao.execute("SELECT * FROM CONTA")
# OPÇÃO 2 cursor = conexao.execute("SELECT * FROM CONTA WHERE ID = 1")
resultado = cursor.fetchall()
print(resultado)
conexao.close()


conexao = sqlite3.connect('contas.sqlite')
conexao.execute("UPDATE CONTA SET CODIGO = '007' WHERE ID = 1")
conexao.commit()
conexao.close()

conexao = sqlite3.connect('contas.sqlite')
conexao.execute("DELETE FROM CONTA WHERE ID = 2")
conexao.commit()
conexao.close()