# name = input("Qual é o nome do filme? ")
# year = int(input("Em que ano foi lançado? "))
# rating = float(input("Qual é a avaliação do filme? "))

# if year < 2000 and rating >= 8.0:
#     print(f"O filme {name} é muito bom. Recomendado!")
# else:
#     print(f"O filme {name} ainda não atingiu uma boa nota.")
    

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        result = 0
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
    result = 0
    
print(f"O resultado da operação é: {result:.2f}")