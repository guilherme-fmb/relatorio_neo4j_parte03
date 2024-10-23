from database import Database
from game_database import GameDatabase

# Criando uma instância da Database com os dados de conexão para o neo4j
db = Database("bolt://44.201.154.123:7687", "neo4j", "sunrise-cable-flower")

db.drop_all()

game_db = GameDatabase(db)

# Criando players
game_db.create_player("Maria")
game_db.create_player("Jonas")
game_db.create_player("Joana")

# Criando matches e suas relações
game_db.create_match("Maria, Guilherme", "Maria")
game_db.create_match("Maria, Joana", "Joana")
game_db.create_match("Joana, Guilherme", "Joana")

# Atualizando o nome de um player
game_db.update_player("Jonas", "Guilherme")

game_db.insert_player_match("Maria", "Maria, Guilherme")
game_db.insert_player_match("Maria", "Maria, Joana")
game_db.insert_player_match("Joana", "Maria, Joana")
game_db.insert_player_match("Joana", "Joana, Guilherme")
game_db.insert_player_match("Guilherme", "Maria, Guilherme")
game_db.insert_player_match("Guilherme", "Joana, Guilherme")

# Deletando player da partida
game_db.delete_player("Joana")
game_db.delete_match("Joana", "Joana, Guilherme")

# Imprimindo todas as infos
print("Jogadores:")
print(game_db.get_players())
print("Partidas:")
print(game_db.get_matches())

# Fechando a conexão com a db
db.close()