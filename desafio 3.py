nome = []
#ter os 5 nomes
nome1 = input("digite o primeiro nome:")
nome2 = input("digite o segundo nome:")
nome3 = input("digite o terceiro nome:")
nome4 = input("digite o quarto nome:")
nome5 = input("digite o quinto nome:")
#comando usado para listar os nomes
nome.append(nome1)
nome.append(nome2)
nome.append(nome3)
nome.append(nome4)
nome.append(nome5)
print("\nOs nomes digitados foram:")
for n in nome:
    print(n)
