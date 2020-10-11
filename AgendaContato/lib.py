from banco import con
from time import sleep
import os


# Validação de Valor Inteiro
def leiaint(valor):
    while True:
        try:
            ent = int(input(valor))
        except:
            print('\033[1;33mDigite um valor inteiro\033[m')
        else:
            break
    return ent
            
# Validação de String
def leiaTexto(txt):
    while True:
        try:
            ent = str(input(txt))
        except:
            if ent.isnumeric():
                print('\033[1;33mDigite um texto válido\033[m')
            else: 
                break  
        return ent 
           
# Cabecalho
def cabecalho(msg):
    print('-'*40)
    print(msg.center(40).upper())
    print('-'*40)

# Menu Principal
def menuprincipal():
    print('''
        [1] - Inserir Contato
        [2] - Listar Contatos
        [3] - Consultar Contato
        [4] - Editar Contato
        [5] - Excluir 
        [6] - Sair
    ''')

# Inserir Contato
def insertContato():
    cabecalho('NOVO CONTATO')   
    try:
        while True:
            regs = leiaTexto('Nº REGISTRO: ').strip()
            if len(regs) < 5  or len(regs) > 5:
                print('\033[1;33mPor favor, insira um registro válido\033[m')
            else:
                break
        while True:
            nome = leiaTexto('NOME: ').strip().title()
            if len(nome) == 0 or nome.isnumeric():
                print('\033[1;33mPreencha o campo\033[m')
            else:
                break
        while True:
            matr = leiaTexto('CHAPA: ').strip().upper()
            if len(matr) <= 4 or len(matr) > 5:
                print('\033[1;33mPor favor, insira uma matricula válida\033[m')
            else:
                break
        while True:
            func = leiaTexto('FUNÇÃO: ').strip().title()
            if len(func) == 0 or func.isnumeric():
                print('\033[1;33mPreencha o campo\033[m')
            else:
                break
        while True:
            period = leiaint('PERÍODO: ')
            if period < 1 or period > 2:
                print('\033[1;33mPor favor, insira um período corretamente\033[m')
            else:
                break
        while True:
            tel = leiaTexto('TELEFONE 1: ').strip()
            if len(tel) < 11 or len(tel) > 14:
                print('\033[1;33mPor favor, Insira um telefone válido\033[m')
            else:
                break
        while True:
            tel_2 = leiaTexto('TELEFONE 2: ').strip()
            if len(tel_2) > 14:
                print('\033[1;33mTelefone Inválido\033[m')
            else:
                break
    except:
        print('\033[1;31mErro na Inserção de dados\033[m')
    else:
        try:
            c = con.cursor()
        except ConnectionError:
            print('\033[1;31mErro na conexão com o banco de dados\033[m')
        else:  
            try:
                ssql = 'SELECT * FROM contato WHERE registro= "'+regs+'"'
                c.execute(ssql)
                inserir = c.fetchall()
            except:
                print('\033[1;33mErro na conferência\033[m')
            else:
                if inserir:
                    print('\033[1;33mCONTATO JÁ EXISTE\033[m')
                else:
                    try:   
                        sql = 'INSERT INTO contato(registro, nome, matricula, funcao, periodo, telefone, telefone_2) SELECT "'+regs+'", "'+nome+'", "'+matr+'", "'+func+'", "'+str(period)+'", "'+tel+'", "'+tel_2+'" WHERE NOT EXISTS (SELECT 1 FROM contato WHERE registro = "'+regs+'")'
                        c.execute(sql)
                    except:
                        print(f'Erro ao inserir contato')
                    else:
                        print('\033[1;32mCONTATO INSERIDO COM SUCESSO!\033[m')
                        con.commit()

# Listar  Contatos
def listarContatos():
    cabecalho('LISTAR CONTATOS')
    try:
        c = con.cursor()
    except ConnectionError:
        print('\033[1;31mErro na conexão com o banco de dados\033[m')
    else:
        try:
            lsql = 'SELECT * FROM contato ORDER BY registro asc'
            c.execute(lsql)
        except:
            print('\033[1;33mErro ao listar contatos\033[m')
        else:
            dados = c.fetchall()
            contador = 0
            limite = 30
            for d in dados:
                print(f'\033[1;36mNº REGISTRO:\033[m{d[1]} \033[1;36mNOME:\033[m{d[2]:<32} \033[1;36mCHAPA:\033[m{d[3]} \033[1;36mFUNÇÃO:\033[m{d[4]:<10} \033[1;36mPERÍODO:\033[m{d[5]} \033[1;36mTELEFONE:\033[m{d[6]} \033[1;36mTELEFONE 2:\033[m{d[7]}')
                print()
                contador += 1
                if contador > limite:
                    contador = 0
                    os.system('pause')
                    os.system('cls')
            con.commit()
            while True:
                v = leiaint('PRESSIONE 8 PARA VOLTAR AO MENU: ')
                if v < 8 or v > 8 :
                    print('\033[1;33mpressione a tecla correta\033[m')
                else:
                    break
            os.system('cls')

# Consultar Contato
def consContato():
    cabecalho('CONSULTAR CONTATO')
    try:
        while True:
            regs = leiaTexto('Nº REGISTRO: ').strip()
            if len(regs) < 5  or len(regs) > 5:
                print('\033[1;33mPor favor, insira um registro válido\033[m')
            else:
                break
    except:
        print('\033[1;31mErro na consulta do contato\033[m')
    else:
        try:
            c = con.cursor()
        except ConnectionError:
            print('\033[1;31mErro na conexão com o banco de dados\033[m')
        else:
            try:
                csql = 'SELECT * FROM contato WHERE registro = "'+regs+'"'
                c.execute(csql)
                mostra = c.fetchall()
            except:
                print('\033[1;33mErro ao Consultar Contato\033[m')  
            else: 
                if mostra:
                    for m in mostra:
                        print(f'\033[1;36mNº REGISTRO:\033[m{m[1]} \033[1;36mNOME:\033[m{m[2]} \033[1;36mCHAPA:\033[m{m[3]} \033[1;36mFUNÇÃO:\033[m{m[4]:^<8} \033[1;36mPERÍODO:\033[m{m[5]} \033[1;36mTELEFONE:\033[m{m[6]} \033[1;36mTELEFONE 2:\033[m{m[7]}')
                else:
                    print('\033[1;33mESSE CONTATO NÃO ESTÁ CADASTRADO\033[m')
                con.commit()

# Editar Contato
def editContato():
    cabecalho('EDITAR CONTATO')
    try:
        while True:
            regs = leiaTexto('Nº REGISTRO: ').strip()
            if len(regs) < 5 or len(regs) > 5:
                print('\033[1;33mPor favor, digite um registro válido\033[m')
            else:
                break
    except:
        print('\033[1;33mErro no contato\033[m')
    else:
        try:
            c = con.cursor()
        except:
            print('\033[1;31mErro na Conexão com Banco de Dados\033[m')
        else:
            try:
                sql = 'SELECT * FROM contato WHERE registro = "'+regs+'"'
                c.execute(sql)
                mostra = c.fetchall()
            except:
                print('\033[1;33mErro na busca do contato\033[m')
            else:
                if mostra:
                    while True:
                        period = leiaint('PERÍODO: ')
                        if period < 1 or period > 2:
                            print('\033[1;33mPor favor, insira um período corretamente\033[m')
                        else:
                            break
                    while True:
                        tel = leiaTexto('TELEFONE 1: ').strip()
                        if len(tel) < 11 or len(tel) > 14:
                            print('\033[1;33mPor favor, Insira um telefone válido\033[m')
                        else:
                            break
                    while True:
                        tel_2 = leiaTexto('TELEFONE 2: ').strip()
                        if len(tel_2) > 14:
                            print('\033[1;33mTelefone Inválido\033[m')
                        else:
                            break
                    esql = 'UPDATE contato SET periodo="'+str(period)+'", telefone="'+tel+'", telefone_2="'+tel_2+'" WHERE registro= "'+regs+'"'
                    c.execute(esql)
                    con.commit()
                    print('\033[1;32mCONTATO ALTERADO COM SUCESSO!\033[m')
                    sleep(1)
                else:
                    print('\033[1;33mCONTATO NÃO ESTÁ CADASTRADO\033[m')

# Deletar Contato
def apagaContato():
    cabecalho('APAGAR CONTATO')
    try:
        while True:
            regs = leiaTexto('Nº Registro que deseja apagar o contato: ').strip()
            if len(regs) < 5 or len(regs) > 5:
                print('\033[1;33mPor favor, digite um registro válido\033[m')
            else:
                break
    except:
        print('\033[1;33mErro na busca do contato\033[m')
    else:
        try:
            c = con.cursor()
        except ConnectionError:
            print('\033[1;31mErro na conexão com o banco de dados\033[m')
        else:
            try:
                sql = 'SELECT * FROM contato WHERE registro = "'+regs+'"'
                c.execute(sql)
                mostra = c.fetchall()
            except:
                print('\033[1;33mErro na busca do contato\033[m')
            else:
                while True:
                    resp = leiaTexto('Tem certeza que deseja apagar o registro [S/N] ?: ').strip().upper()[0]
                    if resp not in 'SN':
                        print('Responda')
                    else:
                        break 
                if resp in 'S':
                    if mostra:
                        try:    
                            dsql =  'DELETE FROM contato WHERE registro = "'+regs+'"'
                            c.execute(dsql)          
                        except:
                            print('\033[1;33mErro ao deletar contato\033[m')
                        else:
                            print('\033[1;32mCONTATO DELETADO COM SUCESSO!\033[m')
                            con.commit()
                    else:
                        print('\033[1;33mCONTATO NÃO ESTÁ CADASTRADO\033[m')
                else:
                    print('nada deletado')
                    
