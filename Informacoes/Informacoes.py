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
    
    resultado = cur.execute(sql)
    print(resultado)
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

    resultado = cur.execute(sql)
    print(resultado)
    input("Pressione ENTER para voltar.")


#--------------------- Média salarial dos professores--------------------------------#
def MediaSalarial(conexao, cur):
    os.system('clear')
    print("-> Média salarial dos professores <-\n")

    sql = '''SELECT cursos.cod_curso, cursos.nome, AVG(professores.salario)
    FROM cursos INNER JOIN professores ON cursos.cod_curso = professores.cod_curso
    GROUP BY cursos.cod_curso, cursos.nome
    ORDER BY cursos.cod_curso;'''

    resultado = cur.execute(sql)
    print(resultado)
    input("Pressione ENTER para voltar.")


#--------------------- Folha de pagamento mensal --------------------------------#
def FolhaDePagamento(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Folha de pagamento <-\n")

    sql = '''SELECT setores.cod_setor, setores.nome, SUM(funcionarios.salario)
    FROM setores INNER JOIN funcionarios ON setores.cod_setor = funcionarios.cod_setor
    GROUP BY setores.cod_setor, setores.nome ORDER BY SUM(funcionarios.salario) DESC;'''

    resultado = cur.execute(sql)
    print(resultado)
    input("Pressione ENTER para voltar.")


#--------------------- Média final das disciplinas de um professor --------------------------------#
def MediaFinal(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Média final das disciplinas de um professor <-\n")


#--------------------- Em quantos cursos cada professor trabalha --------------------------------#
def CursosPorProf(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Em quantos cursos cada professor trabalha <-\n")

    sql = '''SELECT professores.nome, professores.cpf, COUNT(cod_curso)
    FROM professores INNER JOIN disciplinas ON professores.cpf = disciplinas.cpf_professor
    INNER JOIN cursos_disciplinas
    GROUP BY professores.nome, professores.cpf
    ORDER BY qtd_cursos, professor.nome;'''

    resultado = cur.execute(sql)
    print(resultado)
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
    
    resultado = cur.execute(sql)
    print(resultado)
    input("Pressione ENTER para voltar.")



#--------------------- Número total de alunos por curso --------------------------------#
def AlunoPorCurso(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Número total de alunos por curso <-\n")

    sql = '''SELECT cursos.cod_curso, cursos.nome, COUNT(alunos.cpf)
    FROM cursos INNER JOIN alunos ON cursos.cod_curso = alunos.cod_curso
    GROUP BY cursos.cod_curso, cursos.nome
    ORDER BY COUNT(alunos.cpf);'''

    resultado = cur.execute(sql)
    print(resultado)
    input("Pressione ENTER para voltar.")    


#--------------------- Disciplina com a maior taxa --------------------------------#
def TaxaDisciplina(conexao, cur):
    os.system('clear') #Limpa a tela
    print("-> Disciplina com a maior taxa de aprovação/reprovação <-\n")
