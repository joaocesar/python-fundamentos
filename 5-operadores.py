num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritmeticos: + - * / % **
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"Soma de {num1} + {num2} é: {sum}")
print(f"Subtração de {num1} - {num2} é: {sub}")
print(f"Multiplicação de {num1} * {num2} é: {mult}")
print(f"Divisão de {num1} / {num2} é: {div}")

mod = num1 % num2
exp = num1 ** num2

print(f"Resto de {num1} dividido por {num2} é: {mod}")
print(f"Potencia {num1} eleavado a {num2} é: {exp}")

# Comparadores: > < == != >= <=
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
notEqual = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2
print(f"{num1} é maior que {num2}? {bigger}")
print(f"{num1} é menor que {num2}? {smaller}")
print(f"{num1} é igual a {num2}? {equal}")
print(f"{num1} é diferente de {num2}? {notEqual}")
print(f"{num1} é maior ou igual a {num2}? {biggerEqual}")
print(f"{num1} é menor ou igual a {num2}? {smallerEqual}")


# Atribuição: += -= *= /=

