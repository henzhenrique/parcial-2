num1 = float(input("Digite o primeiro número: "))#escolher os numeros
op = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))
#definir as operaçoes da calculadora
if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "erro, não é possivel dividir por 0"
else:
    resultado = "operação invalida"
# mostrar o resultado no final
print("Resultado:", resultado)
