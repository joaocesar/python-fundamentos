# Lista é definida por colchetes []
# Pode conter diferentes tipos de dados
# Pode ser alterada (mutável)

filmeMatrix = ["Matrix", 1999, 8.7, True]

print(filmeMatrix)
print(type(filmeMatrix))
print(filmeMatrix[0])
print(filmeMatrix[1])
print(filmeMatrix[2])
print(filmeMatrix[3])

listaFilmes = ["Matrix", "Top Gun", "Interestelar", "O Poderoso Chefão", "O Senhor dos Anéis"]

# 1 - Buscar os dois primeiros filmes da lista
print(listaFilmes[:2])

# 2 - Buscar o ultimo filme da lista
print(listaFilmes[-1])

# 3 - Buscar filmes até uma determinada posição
print(listaFilmes[:3])

# 4 - Buscar filmes a partir de uma determinada posição
print(listaFilmes[1:4])