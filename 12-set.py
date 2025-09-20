# Set é uma coleção não ordenada de elementos únicos
# Definido por chaves {}
# Não permite elementos duplicados
# Pode ser alterado (mutável)
# Não permite acesso por índices
# Operações matemáticas como união, interseção, diferença e diferença simétrica
# Útil para remover duplicatas de uma lista

filmesSet = {"Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interstellar"}

print(filmesSet)
print(type(filmesSet))

# 1 - Mostrar o tamanho do set
print(len(filmesSet))

# 2 - True e 1, False e 0 são considerados iguais
numerosSet = {1, 2, 3, 4, 5, True, False, 0}
print(numerosSet)
print(len(numerosSet))

# 3 - Adicionar um item ao set
filmesSet.add("Matrix")
print(filmesSet)

# 4 - Remover um item do set
filmesSet.remove("Pulp Fiction")  # Gera erro se o item não existir
print(filmesSet)
filmesSet.discard("O Poderoso Chefão")  # Não gera erro se o item não existir
print(filmesSet)
filmesSet.pop()  # Remove um item aleatório
print(filmesSet)
# filmesSet.clear()  # Remove todos os itens do set
# print(filmesSet)
# del filmesSet  # Deleta o set
# print(filmesSet)  # Gera erro pois o set foi deletado 
