from database.conexao import conectar

def recuperar_carrinho(id_usuario):
    conexao,cursor = conectar()

    cursor.execute("""SELECT 
                        pokemons.id_pokemon,
                        pokemons.nome,
                        pokemons.imagem,
                        pokemons.preco,
                        COUNT(produtos_carrinho.id_pokemon) AS quantidade,
                        carrinhos.id_usuario, 
                        carrinhos.finalizado
                    FROM pokevault.carrinhos
                    INNER JOIN produtos_carrinho ON carrinhos.id_carrinho = produtos_carrinho.id_carrinho
                    INNER JOIN pokemons ON produtos_carrinho.id_pokemon = pokemons.id_pokemon
                    WHERE carrinhos.id_usuario = %s
                    GROUP BY 
                        pokemons.id_pokemon, 
                        pokemons.nome, 
                        pokemons.imagem, 
                        pokemons.preco;""",[id_usuario])

    pokemons=cursor.fetchall()

    conexao.close()

    return pokemons


def adicionar_pokemon_carrinho(id_pokemon,id_carrinho):
    conexao,cursor = conectar()

    cursor.execute("""insert into produtos_carrinho(id_pokemon,quantidade,id_carrinho)
                    values(%s,1,%s)""",[id_pokemon,id_carrinho])

    conexao.commit()
    conexao.close()

    return True


def remover_pokemon_carrinho(id_pokemon,id_carrinho):
        conexao,cursor = conectar()

        cursor.execute("""DELETE FROM produtos_carrinho WHERE id_pokemon = %s AND id_carrinho = %s LIMIT 1;""",(id_pokemon,id_carrinho)) 
        
        conexao.commit()

        conexao.close()
        return True
