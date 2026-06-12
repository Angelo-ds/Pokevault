from database.conexao import conectar

def cadastrar(email, nome, telefone, endereço, senha):
        conexao,cursor = conectar()

        cursor.execute('''INSERT INTO pokevault.usuarios (email,nome,telefone, endereço, senha)
        VALUES(%s, %s, %s, %s, %s);
        ''',[email, nome, telefone, endereço, senha])

        conexao.commit()
        conexao.close()