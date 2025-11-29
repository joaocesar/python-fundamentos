# Lista de filmes

filmes = ["Inception", "The Dark Knight", "Pulp Fiction", "Forrest Gump", "The Matrix"]

for filme in filmes:
    print(f"Filme: {filme}")
print("-----------")
for filme in filmes:
    if filme == "Pulp Fiction":
        break
    print(f"Filme: {filme}")
print("-----------")
for filme in filmes:
    if filme == "Pulp Fiction":
        continue
    print(f"Filme: {filme}")
print("-----------")

