from getpass import getpass
from Verificacoes import *
import os

#--------------------- inscrever aluno --------------------------------#
def InscreverAluno(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Inscrever aluno <-\n")
    print("Por favor, informe:\n")
    
    cpfAluno = input("CPF do aluno: ") #Recebe o cpf do aluno    
    if(VerificaAluno(cur, cpfAluno) == -1): #Verifica se o cpf já foi cadastrado (-1 = NÃO)
        print("\nERRO: Aluno não cadastrado!") #Mensagem de erro 
        input("Pressione ENTER para voltar.")
        return
    
    codDisc = input("Codigo da disciplina: ") #Recebe o código da disciplina  
    if(VerificaDisciplina(cur, codDisc) == -1): #Verifica se a disciplina já foi cadastrada (-1 = NÃO)
        print("\nERRO: Disciplina não cadastrtada!") #Mensagem de erro 
        input("Pressione ENTER para voltar.")
        return
        
    if (VerificaInscricao(cur, codDisc, cpfAluno) == -1): #caso seja a primeira inscrição do aluno
        sql = "INSERT INTO inscritos (cod_disciplina, cpf_aluno, nota, vez) VALUES ( %s, %s, %s, %s)" #Insere na tabela
        data = (codDisc, cpfAluno, 0, 1) #Utiliza os dados do insert
        
        cur.execute(sql, data) #Executa o comando(sql+data)
        conexao.commit() #salva a alteração no banco
    else:
        sql = ('''  UPDATE inscritos
                SET vez = vez+1
                WHERE cod_disciplina == %s AND cpf_aluno == %s ''')
        data = (codDisc, cpfAluno)
        
        cur.execute(sql, data) #Executa o comando(sql+data)
        conexao.commit() #salva a alteração no banco

    print("\nInscrito com sucesso!")
    input("Pressione ENTER para voltar.")


#--------------------- cancelar inscrição --------------------------------#
def CancelarInscricao(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Cancelar incrição de aluno <-\n")
    print("Por favor, informe:\n")
    
    cpfAluno = input("CPF do aluno: ") #Recebe o cpf do aluno    
    if(VerificaAluno(cur, cpfAluno) == -1): #Verifica se o cpf já foi cadastrado (-1 = NÃO)
        print("\nERRO: Aluno não cadastrado!") #Mensagem de erro 
        input("Pressione ENTER para voltar.")
        return
    
    codDisc = input("Codigo da disciplina: ") #Recebe o código da disciplina  
    if(VerificaDisciplina(cur, codDisc) == -1): #Verifica se a disciplina já foi cadastrada (-1 = NÃO)
        print("\nERRO: Disciplina não cadastrada!") #Mensagem de erro 
        input("Pressione ENTER para voltar.")
        return
        
    if (VerificaInscricao(cur, codDisc, cpfAluno) == -1): #caso seja o aluno não esteja inscrito
        print("\nERRO: Aluno não inscrito!") #Mensagem de erro 
        input("Pressione ENTER para voltar.")
        return

    sql = ('''DELETE from inscritos WHERE cod_disciplina == %s AND cpf_aluno == %s ''') 
    data = (codDisc, cpfAluno)
    
    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\Inscrição cancelada com sucesso!")

