from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector as mysql
from Cadastro.MenuCadastro import *
import os

#-------------- se conectando ao mysql --------------------#
conexao = mysql.connect( 
        host="localhost", #endereço de ip do servidor usado
        user="root", #login
        password="password", #senha
        database="universidade"
)
cur = conexao.cursor()

#--------------------- menu --------------------------------#
escolha_inicial = 1
while(escolha_inicial != 0):
    os.system('clear')
    print("-> Sistema de Gerenciamento da Universidade <-\n")
    print("0. Sair")
    print("1. Cadastro")
    print("2. Lançar notas")
    print("3. Informações sobre a universidade")
        
    escolha_inicial = int(input("\nDigite sua escolha: "))
    if(escolha_inicial == 1):
        Cadastro(conexao, cur) #leva ao menu dos cadastros
 
    if(escolha_inicial == 2):
        #Notas(conexao, cur) #chama a função das notas
        print("opção 2")

    if(escolha_inicial == 3):
        #Informacoes(conexao, cur) #chama a função das informações
        print("opção 3")

#-------------- encerra a conexão ao msql --------------------#
cur.close()
conexao.close()