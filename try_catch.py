try:
    numero = float(input("Digite o número de chocolates que você comprou:"))
    colegas = float(input("Digite o número de colegas que existem:"))

    if numero < 0 or colegas <= 0:
        raise ValueError("Certifique-se de inserir valores numéricos válidos e não negativos.")

    resultado = numero / colegas

    if resultado < 0:
        raise ValueError("O resultado da divisão é menor que zero.")

    print("O resultado da divisão é:", resultado)

except ValueError as error:
    print("Ocorreu um erro:", error)
