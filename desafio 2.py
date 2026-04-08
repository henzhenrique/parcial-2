def eh_par(numero):
    if numero % 2 == 0:#pra definir se o numero é par
        return True
    else:
        return False
#pede pra pessoa digitar o numero.
num = int(input("Digite um número: "))
if eh_par(num):
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
