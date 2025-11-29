
filmes = ["Inception", "The Dark Knight", "Pulp Fiction", "Forrest Gump", "The Matrix"]

index = 0
while index < len(filmes):
    filme = filmes[index]
    print(f"Filme: {filme}")
    index += 1
print("-----------")
index = 0
while index < len(filmes):
    filme = filmes[index]
    if filme == "Pulp Fiction":
        break
    print(f"Filme: {filme}")
    index += 1
print("-----------")
index = 0
while index < len(filmes):
    filme = filmes[index]
    if filme == "Pulp Fiction":
        index += 1
        continue
    print(f"Filme: {filme}")
    index += 1
print("-----------")