def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if eh_par(num):
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
