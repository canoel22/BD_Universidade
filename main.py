from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector as mysql
from Cadastro.MenuCadastro import *
from Notas.Notas import *
from Informacoes.MenuInformacoes import *
from Incricoes.MenuInscricoes import *
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
    print("4. Gerenciamento de inscrições em disciplinas")
        
    escolha_inicial = int(input("\nDigite sua escolha: "))
    if(escolha_inicial == 1):
        Cadastro(conexao, cur) #leva ao menu dos cadastros
 
    if(escolha_inicial == 2):
        Notas(conexao, cur) #chama a função das notas

    if(escolha_inicial == 3):
        Informacoes(conexao, cur) #chama a função das informações

    if(escolha_inicial == 4):
        Incricoes(conexao, cur) #chama a função das informações


#-------------- encerra a conexão ao msql --------------------#
cur.close()
conexao.close()