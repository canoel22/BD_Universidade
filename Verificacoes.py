#--------------------- verifica se um setor já foi cadastrado --------------------------------#

def VerificaSetor(cur, codigo):
    cur.execute("SELECT cod_setor FROM setores") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codigos cadastrados
    for linha in codigos_cadastrados: 
        if(linha[0] == codigo): #Verifica se o código já está no banco de dados
            return 0 #Retorna 0 se estiver
    else:
        return -1 #Retorna -1 se não estiver


#--------------------- verifica se um curso já foi cadastrado --------------------------------#

def VerificaCurso(cur, codigo):
    cur.execute("SELECT cod_curso FROM cursos") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codigos cadastrados
    for linha in codigos_cadastrados: 
        if(linha[0] == codigo): #Verifica se o código já está no banco de dados
            return 0 #Retorna 0 se estiver
    else:
        return -1 #Retorna -1 se não estiver
    
    
#--------------------- verifica se um funcionario já foi cadastrado --------------------------------#

def VerificaFunc(cur, cpf):
    cur.execute("SELECT cpf FROM funcionarios") #select em todos os cpf cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpf cadastrados
    for linha in cpf_cadastrados: 
        if(linha[0] == cpf): #Verifica se o cpf já está no banco de dados
            return 0 #Retorna 0 se estiver
    else:
        return -1 #Retorna -1 se não estiver
    
#--------------------- verifica se um professir já foi cadastrado --------------------------------#

def VerificaProf(cur, cpfProf):
    cur.execute("SELECT cpf FROM professores") #select em todos os cpf cadastrados
    cpf_cadastrados = cur.fetchall() #Recebe todos os cpf cadastrados
    for linha in cpf_cadastrados: 
        if(linha[0] == cpfProf): #Verifica se o cpf já está no banco de dados
            return 0 #Retorna 0 se estiver
    else:
        return -1 #Retorna -1 se não estiver