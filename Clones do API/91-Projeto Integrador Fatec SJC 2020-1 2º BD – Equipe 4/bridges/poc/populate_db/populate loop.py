import pymysql
import random
from random_words import RandomWords

cont = 0

# quantidade de registros fakes que vc quer
limit = 10

while(cont < limit):
    # dados do base mysql

    connection = pymysql.connect(host='sabha.com.br',
                                         port=3306,
                                         user='sabha_bridgesusers',
                                         password='@@PI@@F@tec')


    # setando comando run_statement para rodar INSERT/UPDATE etc.

    run_statement = connection.cursor()

    # necessario usar "connection.commit()" ao final da chamada
    rw = RandomWords()
    word = rw.random_word()
    id_pro = 1

    horas = round(random.uniform(1,30),2)
    run_statement.execute("INSERT INTO sabha_bridgesbd.bridges_app_tarefas(nom_tar, fk_pro_id, dur_tar) VALUES('%s', '%s', '%s')" %(word, id_pro, horas))
    connection.commit()

    cont= cont +1
    print(cont)
connection.close()