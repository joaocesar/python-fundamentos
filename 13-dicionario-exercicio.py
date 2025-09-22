prod1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço do produto 1: "))
prod2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço do produto 2: "))
prod3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço do produto 3: "))

produtos = {
    prod1: preco1,
    prod2: preco2,
    prod3: preco3
}
print(produtos)
print(max(produtos, key=produtos.get))
print(min(produtos, key=produtos.get))
print(sum(produtos.values()))
print(sorted(produtos.items()))
print(sorted(produtos.items(), key=lambda item: item[1], reverse=True))
print(sorted(produtos.items(), key=lambda item: item[1]))
average = round(sum(produtos.values()) / len(produtos), 2)
print(average)
print([f"{k}: R$ {v:.2f}" for k, v in produtos.items() if v > average])
print([f"{k}: R$ {v:.2f}" for k, v in produtos.items() if v < average])
