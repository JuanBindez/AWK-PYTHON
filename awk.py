'''
Author: www.github.com/JuanBindez
Description: command awk
Python Version: 3.10
year: 2022
Local: Brazil
OS: Linux
'''


import os
import time

try:

    def awk_test_a(caminho):
        id = "'{print $1}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_b(caminho):
        id = "'{print $2}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_c(caminho):
        id = "'{print $3}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_d(caminho):
        id = "'{print $4}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_e(caminho):
        id = "'{print $5}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_f(caminho):
        id = "'{print $6}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_g(caminho):
        id = "'{print $7}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_h(caminho):
        id = "'{print $8}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_i(caminho):
        id = "'{print $9}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()


    def awk_test_j(caminho):
        id = "'{print $10}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()

    def awk_test_k(caminho):
        id = "'{print $1$2$3$4$5$6$7$8$10}'"
        os.system('awk -F " " {0} {1}'.format(id, caminho))
        menu_header()

    def desenho_header():
        print(
            '''
                           _              ____        _   _                 
             __ ___      _| | __    _    |  _ \ _   _| |_| |__   ___  _ __  
            / _` \ \ /\ / / |/ /  _| |_  | |_) | | | | __| '_ \ / _ \| '_ \ 
           | (_| |\ V  V /|   <  |_   _| |  __/| |_| | |_| | | | (_) | | | |
            \__,_| \_/\_/ |_|\_\   |_|   |_|    \__, |\__|_| |_|\___/|_| |_|
                                                |___/                       
                    
            '''
        )


    def menu_header():
        desenho_header()
        print(
            '''
                                *        Digite De 1 a 10
                                * [Ctrl + c ] Para Encerrar o Programa
                                * [0] Para Ver Tudo
            '''
        )


        escolha = int(input(">"))

        match escolha:
            case 1:
                awk_test_a(nome_arquivo)

            case 2:
                awk_test_b(nome_arquivo)

            case 3:
                awk_test_c(nome_arquivo)

            case 4:
                awk_test_d(nome_arquivo)

            case 5:
                awk_test_e(nome_arquivo)

            case 6:
                awk_test_f(nome_arquivo)

            case 7:
                awk_test_g(nome_arquivo)

            case 8:
                awk_test_h(nome_arquivo)

            case 9:
                awk_test_i(nome_arquivo)

            case 10:
                awk_test_j(nome_arquivo)

            case 0:
                awk_test_k(nome_arquivo)

            case _:
                print("Digite Apenas Até 10")



    desenho_header()
    nome_arquivo = str(input('Digite o Nome Do Arquivo ou Caminho\n>'))
    menu_header()




except KeyboardInterrupt:
    print("Você Encerrou o Programa !")