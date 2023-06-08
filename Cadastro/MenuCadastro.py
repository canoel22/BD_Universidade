from Cadastro.Cadastros import *
import os

#--------------------- menu de cadastros --------------------------------#
def Cadastro(conexao, cur):
    escolha_usuario = 1
    while(escolha_usuario != 0):
        os.system('clear')
        print("-> Cadastros diponíveis <-\n")
        print("0. Voltar")
        print("1. Cadastro de setor")
        print("2. Cadastro de curso")
        print("3. Cadastro de funcionário administrativo")
        print("4. Cadastro de professor")
        print("5. Cadastro de aluno")
        print("6. Cadastro de disciplina")
        
        escolha_usuario = int(input("\nDigite sua escolha: "))
        if(escolha_usuario == 1):
            CadastroSetor(conexao, cur)
        if(escolha_usuario == 2):
            CadastroCurso(conexao, cur)
        if(escolha_usuario == 3):
            CadastroFunc(conexao, cur)
        if(escolha_usuario == 4):
            CadastroProf(conexao, cur)
        if(escolha_usuario == 5):
            CadastroAluno(conexao, cur)
        if(escolha_usuario == 6):
            CadastroDisc(conexao, cur)