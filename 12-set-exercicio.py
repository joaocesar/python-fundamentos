num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))
num3 = int(input("Digite o terceiro número:\n"))
num4 = int(input("Digite o quarto número:\n"))
num5 = int(input("Digite o quinto número:\n"))

numeros = {num1, num2, num3, num4, num5}
print(numeros)
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(sorted(numeros))
print(sorted(numeros, reverse=True))