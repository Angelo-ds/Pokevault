from database.conexao import conectar

def cadastrar(email, nome, telefone, endereco, senha):
        conexao,cursor = conectar()

        cursor.execute('''INSERT INTO pokevault.usuarios (email,nome,telefone, endereco, senha)
        VALUES(%s, %s, %s, %s, %s);
        ''',[email, nome, telefone, endereco, senha])
        
        id= cursor.lastrowid

        cursor.execute('''INSERT INTO carrinhos (id_usuario,finalizado)
                          VALUES(%s,0)''',[id])

        conexao.commit()
        conexao.close()

def logar(login, senha):
        conexao,cursor = conectar()
        cursor.execute("""
                SELECT * FROM usuarios WHERE email = %s and senha = %s;
            """,
            [login, senha])
        
        resultado = cursor.fetchone()
        conexao.close()
        return resultado   