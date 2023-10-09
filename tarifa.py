def calcular_conta(nome, consumo):
    if consumo <= 20:
        tarifa = 1.6
    elif consumo <= 50:
        tarifa = 2.8
    else:
        tarifa = 4.2

    valor_mensal = consumo * tarifa

    if valor_mensal < 100:
        valor_mensal *= 0.95
    elif valor_mensal > 200:
        valor_mensal *= 1.1

    return valor_mensal

def inserir_dados(nome, consumo):
    conta_mensal = calcular_conta(nome, consumo)
    database.append({"nome": nome, "consumo": consumo, "conta_mensal": conta_mensal})

database = []

try:
    nome = input("Digite o nome do responsável pelo medidor: ")
    if not nome:
        raise ValueError("Nome não pode ser vazio.")

    consumo_str = input("Digite o volume consumido em metros cúbicos: ")
    if not consumo_str:
        raise ValueError("O valor do consumo não pode ser vazio.")

    consumo = float(consumo_str)
    if isnan(consumo):
        raise ValueError("Digite um valor de consumo válido.")

    inserir_dados(nome, consumo)

    print("Conta Mensal para", nome)
    print("Consumo:", consumo, "m³")
    print("Valor Mensal:", database[0]["conta_mensal"], "R$")
except Exception as error:
    print("Ocorreu um erro:", str(error))
