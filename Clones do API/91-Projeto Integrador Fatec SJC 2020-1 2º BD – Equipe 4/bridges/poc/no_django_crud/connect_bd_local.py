import pymysql

# dados do base mysql

connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='56565665665')


# setando comando run_statement para rodar INSERT/UPDATE etc.

run_statement = connection.cursor()

# necessario usar "connection.commit()" ao final da chamada

nome = 'João Silva'
horas = 220
run_statement.execute("INSERT INTO polls.daniel(name) VALUES('%s')" %(nome))
connection.commit()