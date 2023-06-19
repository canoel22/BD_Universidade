from getpass import getpass
from tabulate import tabulate
from Informacoes.MenuInformacoes import *
from Verificacoes import *
import os

#--------------------- Turmas com mais alunos do campus --------------------------------#
def TurmaCheia(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Turmas com mais alunos do campus <-\n")

    sql = '''SELECT nome, count(cpf_aluno)
        FROM disciplinas INNER JOIN inscritos
        ON inscritos.cod_disciplina = disciplinas.cod_disciplina
        GROUP BY nome HAVING COUNT(cpf_aluno) >= ALL (
        SELECT COUNT(cpf_aluno)
        FROM disciplinas INNER JOIN inscritos
        ON inscritos.cod_disciplina = disciplinas.cod_disciplina
        GROUP BY nome);'''
    
    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")


#--------------------- Quantidade de professores ativos em cada curso --------------------------------#
def ProfsAtivos(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Quantidade de professores ativos em cada curso <-\n")

    sql = '''SELECT cursos.cod_curso, cursos.nome, count(professores.cpf) 
    FROM cursos INNER JOIN professores ON professores.cod_curso = cursos.cod_curso
    WHERE professores.ativo = 1
    GROUP BY cursos.cod_curso, cursos.nome
    ORDER BY cursos.cod_curso;'''

    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")


#--------------------- Média salarial dos professores--------------------------------#
def MediaSalarial(conexao, cur):
    os.system('clear')
    print("-> Média salarial dos professores <-\n")

    sql = '''SELECT cursos.cod_curso, cursos.nome, AVG(professores.salario)
    FROM cursos INNER JOIN professores ON cursos.cod_curso = professores.cod_curso
    GROUP BY cursos.cod_curso, cursos.nome
    ORDER BY cursos.cod_curso;'''

    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")


#--------------------- Folha de pagamento mensal --------------------------------#
def FolhaDePagamento(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Folha de pagamento <-\n")

    sql = '''SELECT setores.cod_setor, setores.nome, SUM(funcionarios.salario)
    FROM setores INNER JOIN funcionarios ON setores.cod_setor = funcionarios.cod_setor
    GROUP BY setores.cod_setor, setores.nome ORDER BY SUM(funcionarios.salario) DESC;'''

    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")


#--------------------- Média final das disciplinas de um professor --------------------------------#
def MediaFinal(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Média final das disciplinas de um professor <-\n")

    print("Por favor, informe:\n")
    cpf_professor = input("CPF do professor: ")

    if(VerificaProf(cur, cpf_professor) == -1): #Verifica se o prof já foi cadastrado (-1 = NÃO)
        print("\nERRO: Professor não cadastrado!") #Mensagem de erro pra codigo já cadastrado
        input("Pressione ENTER para voltar.")
        return

    sql1 = f'''CREATE TEMPORARY TABLE t2 (
        SELECT professores.nome AS nome_p, cod_disciplina, disciplinas.nome AS nome_d
        FROM professores INNER JOIN disciplinas
        ON cpf = '{cpf_professor}'
    );'''

    sql2 = '''SELECT nome_p, nome_d, AVG(nota) AS media
    FROM t2 INNER JOIN inscritos
    ON t2.cod_disciplina = inscritos.cod_disciplina
    GROUP BY nome_p, nome_d;'''

    sql3 = '''DROP table t2'''
    
    cur.execute(sql1)
    cur.execute(sql2)
    resultado = cur.fetchall()
    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    cur.execute(sql3)
    input("Pressione ENTER para voltar.")


#--------------------- Em quantos cursos cada professor trabalha --------------------------------#
def CursosPorProf(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Em quantos cursos cada professor trabalha <-\n")


    sql = '''SELECT professores.nome, professores.cpf, COUNT(cursos_disciplinas.cod_curso) AS qtd_cursos
    FROM professores INNER JOIN disciplinas ON professores.cpf = disciplinas.cpf_professor
    INNER JOIN cursos_disciplinas
    GROUP BY professores.nome, professores.cpf
    ORDER BY qtd_cursos, professores.nome;'''

    cur.execute(sql)
    resultado = cur.fetchall()
    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
   
    input("Pressione ENTER para voltar.")

#--------------------- Professor mais antigo --------------------------------#
def ProfAntigo(conexao, cur):
    os.system('clear')
    print("-> Professor mais antigo <-\n")

    sql = '''SELECT cpf, nome, data_contratacao 
    FROM professores AS prof1
    WHERE data_contratacao < ALL
        (SELECT data_contratacao 
        FROM professores AS prof2
        WHERE prof1.cpf <> prof2.cpf);'''
    
    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")



#--------------------- Número total de alunos por curso --------------------------------#
def AlunoPorCurso(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Número total de alunos por curso <-\n")

    sql = '''SELECT cursos.cod_curso, cursos.nome, COUNT(alunos.cpf)
    FROM cursos INNER JOIN alunos ON cursos.cod_curso = alunos.cod_curso
    GROUP BY cursos.cod_curso, cursos.nome
    ORDER BY COUNT(alunos.cpf);'''

    cur.execute(sql)
    resultado = cur.fetchall()

    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    input("Pressione ENTER para voltar.")   


#--------------------- Disciplina com a maior taxa --------------------------------#
def TaxaDisciplina(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Disciplina com a maior taxa de aprovação/reprovação <-\n")
    input("Pressione ENTER para voltar.")
