from getpass import getpass
from Verificacoes import *
import os

#--------------------- cadastro de um setor --------------------------------#
def Notas(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Lançamento de notas <-\n")
    print("Por favor, informe:\n")
    
    cpfAluno = input('CPF do aluno: ')
    if(VerificaAluno(cur, cpfAluno) == -1): #Verifica se o aluno já foi cadastrado (-1 = NÃO)
        print("\nERRO: Aluno não cadastrado!") #Mensagem de erro pra aluno não cadastrado
        input("Pressione ENTER para voltar.")
        return
    else:
        if(VerificaAtividade(cur, cpfAluno) == -1): #Verifica se o aluno jestá ativo (-1 = NÃO)
            print("\nERRO: Aluno inativo!") #Mensagem de erro pra aluno inativo
            input("Pressione ENTER para voltar.")
            return

    codDisc = int(input('Código da disciplina: '))
    if(VerificaDisciplina(cur, codDisc) == -1): #Verifica se o curso já foi cadastrado (-1 = NÃO)
        print("\nERRO: Disciplina não cadastrada!") #Mensagem de erro pra disciplina não encontrada
        input("Pressione ENTER para voltar.")
        return
    
    nota = float(input('Nota: ')) #Verifica se a nota é válida
    while nota < 0 or nota > 10:
        print('Nota inválida! Tente novamente!')
        nota = float(input('Digite a nota: '))


    if(VerificaInscricao(cur, codDisc, cpfAluno) == -1): #Verifica se o aluno está inscrito na disciplina (-1 = NÃO)
        print("\nERRO: Aluno não inscrito na disciplina!") #Mensagem de erro pra aluno não incrito
        input("Pressione ENTER para voltar.")
        return

    sql = ("UPDATE incritos SET nota = %s WHERE cpf_aluno = %s AND cod_disciplina = %d ")
    data = (nota, cpfAluno, codDisc)

    cur.execute(sql, data) #Executa o comando(sql+data)
    conexao.commit() #salva a alteração no banco

    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")

