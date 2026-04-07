# Função para calcular os juros simples
def calcular_juros(principal, taxa_juros, tempo):
    juros = principal * taxa_juros * tempo
    montante = principal + juros
    return juros, montante

# Entrada de dados
principal = float(input("Valor principal (em R$): "))
taxa_juros = float(input("Taxa de juros (% ao mês): ")) / 100  # Convertendo para decimal
tempo = float(input("Tempo (em meses): "))

# Cálculo
juros, montante = calcular_juros(principal, taxa_juros, tempo)

# Resultado
print(f"Juros: R${juros:.2f}")
print(f"Montante final: R${montante:.2f}")

