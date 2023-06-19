#--------------------- verifica se um setor já foi cadastrado --------------------------------#

def VerificaSetor(cur, codigo):
    cur.execute(f"SELECT cod_setor FROM setores WHERE cod_setor = {codigo}") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codigos cadastrados
    if len(codigos_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver

#--------------------- verifica se um curso já foi cadastrado --------------------------------#

def VerificaCurso(cur, codigo):
    cur.execute(f"SELECT cod_curso FROM cursos WHERE cod_curso = {codigo}") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codigos cadastrados
    if len(codigos_cadastrados) == 1:
        return 0
  
    return -1 #Retorna -1 se não estiver
 
#--------------------- verifica se um funcionario já foi cadastrado --------------------------------#

def VerificaFunc(cur, cpf):
    cur.execute(f"SELECT cpf FROM funcionarios WHERE cpf = {cpf}") #select em todos os cpf cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpf cadastrados
    if len(cpf_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver
    
#--------------------- verifica se um professor já foi cadastrado --------------------------------#

def VerificaProf(cur, cpfProf):
    cur.execute(f"SELECT cpf FROM professores WHERE cpf = {cpfProf}") #select em todos os cpf cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpf cadastrados
    if len(cpf_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver
    

#--------------------- verifica se um aluno já foi cadastrado --------------------------------#

def VerificaAluno(cur, cpfAluno):
    cur.execute(f"SELECT cpf FROM alunos WHERE cpf = {cpfAluno}") #select em todos os cpf cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpf cadastrados
    if len(cpf_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver
    
    
#--------------------- verifica se um aluno está ativo --------------------------------#

def VerificaAtividade(cur, cpfAluno):
    cur.execute(f"SELECT ativo FROM alunos WHERE cpf = {cpfAluno}") #select em todos os cpfs cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpfs inscritos na disciplina
    if len(cpf_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver
    

#--------------------- verifica se uma disciplina já foi cadastrado --------------------------------#

def VerificaDisciplina(cur, codDisc):
    cur.execute(f"SELECT cod_disciplina FROM disciplinas WHERE cod_disciplina = {codDisc}") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codigos cadastrados
    if len(codigos_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver
    

#--------------------- verifica se um aluno foi inscrito na disciplina --------------------------------#

def VerificaInscricao(cur, codDisc, cpfAluno):
    cur.execute(f"SELECT cpf_aluno FROM inscritos WHERE cod_disciplina = {codDisc} AND cpf_aluno={cpfAluno}") #select em todos os cpfs cadastrados
    cpfs_cadastrados = cur.fetchall() #Recebe todos os cpfs inscritos na disciplina
    if len(cpfs_cadastrados) == 1:
        return 0
    else:
        return -1 #Retorna -1 se não estiver