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
        print("\nERRO: Código já cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO setores (cod_setor, nome) VALUES ( %s, %s)" #Insere na tabela setores
    data = (codigo, nome) #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cadastro de um curso --------------------------------#

def CadastroCurso(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cadastro de curso <-\n")
    print("Por favor, informe:\n")
    
    nome = input("Nome: ") #Recebe o nome
    codigo = input("Código: ") #Recebe o código do curso
    ano = input("Ano de início: ") # Recebe o ano de início
    
    if(VerificaCurso(cur, codigo) == 0): #Verifica se o curso já foi cadastrado (0 = SIM)
        print("\nERRO: Código já cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO cursos (cod_setor, nome, ano_inicio) VALUES ( %s, %s, %s)" #Insere na tabela setores
    data = (codigo, nome, ano) #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cadastro de um funcionario --------------------------------#

def CadastroFunc(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cadastro de funcionário <-\n")
    print("Por favor, informe:\n")
    
    nome = input("Nome: ") #Recebe o nome
    cpf = input("CPF: ") #Recebe o código do curso
    endereco = input("Endereço: ") # Recebe o endereço
    salario = input("Salário: ") # Recebe o salário
    cod_setor = input("Código do setor: ") # Recebe o setor
    
    if(VerificaFunc(cur, cpf) == 0): #Verifica se o curso já foi cadastrado (0 = SIM)
        print("\nERRO: CPF já cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
    
    if(VerificaSetor(cur, cod_setor) == -1): #Verifica se o setor já foi cadastrado (-1 = NÃO)
        print("\nERRO: Setor não cadastrado!") #Mensagem de erro pra setor não encontrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO funcionarios (cpf, nome, endereco, salario, cod_setor) VALUES ( %s, %s, %s, %s, %s)" #Insere na tabela setores
    data = (cpf, nome, endereco, salario, cod_setor) #Utiliza os dados do insert

    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cadastro de um professor --------------------------------#

def CadastroProf(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cadastro de professor <-\n")
    print("Por favor, informe:\n")
    
    nome = input("Nome: ") #Recebe o nome
    cpf = input("CPF: ") #Recebe o código do curso
    telefone = input("Telefone: ") #Recebe o telefone
    endereco = input("Endereço: ") # Recebe o endereço
    salario = input("Salário: ") # Recebe o salário
    data_contratacao = input("Data de contratação: ") #Recebe a data de contratação
    cod_curso = input("Código do curso: ") # Recebe o setor
    
    if(VerificaFunc(cur, cpf) == 0): #Verifica se o curso já foi cadastrado (0 = SIM)
        print("\nERRO: CPF já cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
    
    if(VerificaCurso(cur, cod_curso) == -1): #Verifica se o curso já foi cadastrado (-1 = NÃO)
        print("\nERRO: Curso não cadastrado!") #Mensagem de erro pra curso não encontrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO professores (cpf, nome, telefone, endereco, salario, data_contratacao, ativo, cod_curso) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)" #Insere na tabela setores
    data = (cpf, nome, endereco, salario, data_contratacao, "Ativo", cod_curso) #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cadastro de um aluno --------------------------------#

def CadastroAluno(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cadastro de alunos <-\n")
    print("Por favor, informe:\n")
    
    nome = input("Nome: ") #Recebe o nome
    cpf = input("CPF: ") #Recebe o código do curso
    telefone = input("Telefone: ") #Recebe o telefone
    endereco = input("Endereço: ") # Recebe o endereço

    
    if(VerificaFunc(cur, cpf) == 0): #Verifica se o curso já foi cadastrado (0 = SIM)
        print("\nERRO: CPF já cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return
        
    sql = "INSERT INTO alunos (cpf, nome, telefone, endereco, ativo) VALUES ( %s, %s, %s, %s, %s)" #Insere na tabela setores
    data = (cpf, nome, endereco, "Ativo") #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cadastro de um aluno --------------------------------#

def CadastroDisc(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cadastro de disciplina <-\n")
    print("Por favor, informe:\n")
    
    cod_disc = input("Código da disciplina: ") # Recebe a disciplina
    nome = input("Nome: ")
    cpfProf = input("CPF do professor:")

    if(VerificaProf(cur, cpfProf) == -1): #Verifica se o setor já foi cadastrado (-1 = NÃO)
        print("\nERRO: Setor não cadastrado!") #Mensagem de erro pra setor não encontrado
        input("Pressione ENTER para voltar.")
        return
    
    sql = "INSERT INTO disciplinas (cod_disc, nome, cpfProf) VALUES ( %s, %s, %s)" #Insere na tabela setores
    data = (cod_disc, nome, cpfProf) #Utiliza os dados do insert
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")
