import pymysql

# dados do base mysql

connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
                                     port=3306,
                                     user='ufgpsjx1cswrmye3',
                                     password='ZoKM7HXwAaZAgd9ugpTr')


# setando comando run_statement para rodar INSERT/UPDATE etc.

run_statement = connection.cursor()

# necessario usar "connection.commit()" ao final da chamada