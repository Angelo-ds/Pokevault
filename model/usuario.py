from database.conexao import conectar

def cadastrar(self):
        conexao,cursor = conectar()

        cursor.execute('''INSERT INTO pokevault.usuarios (email,nome,telefone, endereço, senha)
        VALUES(%s, %s, %s, %s, %s);
        ''',[self.usuario, self.senha, self.nome])

        conexao.commit()
        conexao.close()