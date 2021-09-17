from connect_bd import connection, run_statement
nome = 'João Silva'
horas = 220
run_statement.execute("INSERT INTO bvzfdagnfqepipz70gyw.001fun(nome, limite_horas_mes) VALUES('%s', '%s')" %(nome, horas))
connection.commit()
