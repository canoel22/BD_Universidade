from Inscricoes.Inscricoes import *
import os

#--------------------- menu de cadastros --------------------------------#
def Inscricoes(conexao, cur):
    escolha_usuario = 1
    while(escolha_usuario != 0):
        os.system('clear')
        print("-> Gerenciamento de inscrições <-\n")
        print("0. Voltar")
        print("1. Inscrever aluno")
        print("2. Cancelar inscrição")
        
        escolha_usuario = int(input("\nDigite sua escolha: "))
        if(escolha_usuario == 1):
            InscreverAluno(conexao, cur)
        if(escolha_usuario == 2):
            CancelarInscricao(conexao, cur)
