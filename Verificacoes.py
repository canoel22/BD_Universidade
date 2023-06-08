#--------------------- verifica se um setor já foi cadastrado --------------------------------#

def VerificaSetor(cur, codigo):
    cur.execute("SELECT cod_setor FROM setores") #select em todos os codigos cadastrados
    codigos_cadastrados = cur.fetchall() #Recebe todos os codgigos cadastrados
    for linha in codigos_cadastrados: 
        if(linha[0] == codigo): #Verifica se o código já está no banco de dados
            return 0 #Retorna 0 se estiver
    else:
        return -1 #Retorna -1 se não estiver


#--------------------- verifica se um curso já foi cadastrado --------------------------------#

