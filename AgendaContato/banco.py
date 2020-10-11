import sqlite3

try:
    con = sqlite3.Connection('agenda.db')
    c = con.cursor()
except ConnectionError:
    print('\033[1;31mErro ao tentar conectar-se ao banco\033[m')
else:
    try:  
        sql = ''' CREATE TABLE IF NOT EXISTS contato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            registro VARCHAR(5),
            nome VARCHAR(50),
            matricula VARCHAR(5),
            funcao VARCHAR(25),
            periodo INTEGER(1),
            telefone VARCHAR(14),
            telefone_2 VARCHAR(14));
            '''
        c.execute(sql)
    except:
        print('Erro ao criar tabela')
    else:
        print('ok')