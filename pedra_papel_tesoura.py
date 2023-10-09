from random import choice
import os


comp_vitorias = 0
jogador_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    if esc_jogador in ["Pedra", "PEDRA", "pedra"]: esc_jogador = "pedra"
    elif esc_jogador in ["Papel", "PAPEL", "papel"]: esc_jogador = "papel"
    elif esc_jogador in ["Tesoura", "TESOURA", "tesoura"]: esc_jogador = "tessoura"
    else:
        print("Opcao Invalida. Tente Novamente")
        Opcao_Jogador()
    return esc_jogador

def Opcao_Computador():
    esc_computador = choice(["pedra", "papel", "tesoura"])
    return esc_computador


while True:

    print("---------------")

    esc_computador = Opcao_Computador()
    esc_jogador = Opcao_Jogador()

    print("---------------")

    os.system('cls')

    if (esc_jogador == "papel") and (esc_computador == "pedra"):
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1

    elif (esc_jogador == "pedra") and (esc_computador == "tesoura"):
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1

    elif (esc_jogador == "tesoura") and (esc_computador == "papel"):
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1

    elif (esc_jogador == esc_computador):
        print(f"O Jogador escolheu {esc_jogador} e o Adversario escolheu {esc_computador}, sendo o Resultado: Empate")

    else:
        print(f"O Jogador escolheu {esc_jogador} e o Adversario escolheu {esc_computador}, sendo o Resultado: Computador Ganhou")
        comp_vitorias += 1
    
    print("-----------------")

    print(f"Vitorias do Jogador: {jogador_vitorias}")
    print(f"Vitorias do Computador: {comp_vitorias}")

    print("-----------------")

    esc_jogador = input("Voce quer jogar novamente (s/n)")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "N", "n"]:
        break
    else:
        break