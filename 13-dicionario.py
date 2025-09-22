# Dicionário é uma coleção de pares chave-valor 
# Definido por chaves {}
# Pode conter diferentes tipos de dados
# Pode ser alterado (mutável)

import pprint

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

pprint = pprint.PrettyPrinter(depth=4)
pprint.pprint(filmeDict)
pprint.pprint(type(filmeDict))
pprint.pprint(len(filmeDict))

# 1 - Acessar valores pelas chaves
pprint.pprint(filmeDict["name"])
pprint.pprint(filmeDict.get("yearLaunch"))

# 2 - Listar as chaves do dicionário
pprint.pprint(filmeDict.keys())

# 3 - Listar os valores do dicionário
pprint.pprint(filmeDict.values())

# 4 - Listar os itens (chave-valor) do dicionário
pprint.pprint(filmeDict.items())

# 5 - Adicionar um novo par chave-valor
filmeDict["duration"] = 148  # duração em minutos
pprint.pprint(filmeDict)

# 6 - Modificar um valor existente
filmeDict["noteMovie"] = 9.0
pprint.pprint(filmeDict)

# 7 - Remover um par chave-valor
filmeDict.pop("isAvailable")
pprint.pprint(filmeDict)
del filmeDict["awards"]
pprint.pprint(filmeDict)
# filmeDict.clear()  # Remove todos os itens do dicionário
# pprint.pprint(filmeDict)
# del filmeDict  # Deleta o dicionário
# pprint.pprint(filmeDict)  # Gera erro pois o dicionário foi deletado
