from lib import cabecalho, menuprincipal, leiaint, insertContato, listarContatos, consContato, editContato, apagaContato
from time import sleep
import os

while True:
    cabecalho('agenda vb')
    menuprincipal()
    op = leiaint('ESCOLHA UMA OPÇÃO: ')
    os.system('cls')
    if op == 1:
        insertContato()
        sleep(1.5)
        os.system('cls')
    elif op == 2:
        listarContatos()    
    elif op == 3:
        consContato()
    elif op == 4:
        editContato()
        sleep(1.5)
        os.system('cls')
    elif op == 5:
        apagaContato()
        sleep(1.5)
        os.system('cls')
    elif op == 6:
        print('Finalizando...')
        sleep(2)
        os.system('cls')
        print('Programa Encerrado')
        break
    else:
        print('\033[1;31mOpção Inválida, Tente Novamente\033[m')
