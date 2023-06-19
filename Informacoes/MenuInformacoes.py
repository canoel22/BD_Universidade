from Informacoes.Informacoes import *
import os

#--------------------- menu de cadastros --------------------------------#
def Informacoes(conexao, cur):
    escolha_usuario = 1
    while(escolha_usuario != 0):
        os.system('clear')
        print("-> Informações <-\n")
        print("0. Voltar")
        print("1. Turma com mais alunos do campus")
        print("2. Quantidade de professores ativos em cada curso")
        print("3. Média salarial dos professores")
        print("4. Folha de pagamento mensal")
        print("5. Média final das disciplinas de um professor ")
        print("6. Em quantos cursos cada professor trabalha ")
        print("7. Professor mais antigo da instituição ")
        print("8. Número total de alunos por curso ")
        print("9. Disciplina com maior taxa de aprovação/reprovação ")
        
        escolha_usuario = int(input("\nDigite sua escolha: "))
        if(escolha_usuario == 1):
            TurmaCheia(conexao, cur)
        if(escolha_usuario == 2):
            ProfsAtivos(conexao, cur)
        if(escolha_usuario == 3):
            MediaSalarial(conexao, cur)
        if(escolha_usuario == 4):
            FolhaDePagamento(conexao, cur)
        if(escolha_usuario == 5):
            MediaFinal(conexao, cur)
        if(escolha_usuario == 6):
            CursosPorProf(conexao, cur)
        if(escolha_usuario == 7):
            ProfAntigo(conexao, cur)
        if(escolha_usuario == 8):
            AlunoPorCurso(conexao, cur)
        if(escolha_usuario == 9):
            TaxaDisciplina(conexao, cur)