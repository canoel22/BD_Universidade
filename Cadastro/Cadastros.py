from getpass import getpass
from Cadastro.MenuCadastro import *
from Verificacoes import *
import os

#--------------------- cadastro de um setor --------------------------------#
def CadastroSetor(conexao, cur):
    os.system('clear') #limpa a tela
    print("-> Cadastro de setor <-\n")
    print("Por favor, informe:\n")
    
    nome=input("Nome: ") #Recebe o nome
    codigo = input("Código: ") #Recebe o código do setor
    
    if(VerificaSetor(cur, codigo) == 0): #Verifica se o setor já foi cadastrado (0 = SIM)
        print("\nERRO: Código já cadastrado!") #mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO setores (cod_setor, nome) VALUES ( %s, %s)" #Insere na tabela setores
    data = (codigo, nome) #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


def CadastroCurso(conexao, cur):
    pass


def CadastroFunc(conexao, cur):
    pass


def CadastroProf(conexao, cur):
    pass


def CadastroAluno(conexao, cur):
    pass


def CadastroDisc(conexao, cur):
    pass

