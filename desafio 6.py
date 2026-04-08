def conversor():
    opcoes = {
        '1': ("Segundos para Horas", 1/3600),# as formulas para conversão
        '2': ("Horas para Segundos", 3600),
        '3': ("Minutos para Horas", 1/60),
        '4': ("Horas para Minutos", 60),
        '5': ("Minutos para Segundos", 60),
        '6': ("Segundos para Minutos", 1/60)
    }

    while True:
        print("\n" + "\n".join([f"{k}: {v[0]}" for k, v in opcoes.items()]) + "\n0: Sair")
        escolha = input("Escolha (0-6): ")#pra pessoa escolher oque quer transformar
#
        if escolha == '0': break
        if escolha in opcoes:
            valor = float(input(f"Valor para {opcoes[escolha][0]}: "))
            print(f"Resultado: {valor * opcoes[escolha][1]:.2f}")
        else:
            print("Opção inválida!")

