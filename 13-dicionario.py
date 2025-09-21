# Dicionário é uma coleção de pares chave-valor 
# Definido por chaves {}
# Pode conter diferentes tipos de dados
# Pode ser alterado (mutável)

filmeDict = {
    "name": "Inception",
    "yearLaunch": 2010,
    "noteMovie": 8.8,
    "genre": ["Action", "Sci-Fi", "Thriller"],
    "director": "Christopher Nolan",
    "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "awards": {
        "Oscar": 4,
        "BAFTA": 3,
        "Golden Globe": 4
    },
    "isAvailable": True
}

print(filmeDict)
print(type(filmeDict))
print(len(filmeDict))

# 1 - Acessar valores pelas chaves
print(filmeDict["name"])
print(filmeDict.get("yearLaunch"))

# 2 - Listar as chaves do dicionário
print(filmeDict.keys())

# 3 - Listar os valores do dicionário
print(filmeDict.values())

# 4 - Listar os itens (chave-valor) do dicionário
print(filmeDict.items())

# 5 - Adicionar um novo par chave-valor
filmeDict["duration"] = 148  # duração em minutos
print(filmeDict)

# 6 - Modificar um valor existente
filmeDict["noteMovie"] = 9.0
print(filmeDict)

# 7 - Remover um par chave-valor
filmeDict.pop("isAvailable")
print(filmeDict)
del filmeDict["awards"]
print(filmeDict)
# filmeDict.clear()  # Remove todos os itens do dicionário
# print(filmeDict)
# del filmeDict  # Deleta o dicionário
# print(filmeDict)  # Gera erro pois o dicionário foi deletado
