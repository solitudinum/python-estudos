import random
import os

# ===== ESTADO INICIAL =====
economia = 100
exercito = 50
populacao = 1000
estabilidade = 70
ano = 2026

jogando = True


# ===== FUNÇÕES =====

def limpar_tela():
    os.system("cls")  # Windows


def mostrar_status(ano, economia, exercito, populacao, estabilidade):
    print("\n======= STATUS DO PAÍS =======")
    print(f"Ano: {ano}")
    print(f"Economia: {economia}")
    print(f"Exército: {exercito}")
    print(f"População: {populacao}")
    print(f"Estabilidade: {estabilidade}")
    print("===============================")


def investir_economia(economia, estabilidade):
    economia += 20
    estabilidade += 2
    print("Investimento feito na economia.")
    return economia, estabilidade


def investir_exercito(economia, exercito, estabilidade):
    economia -= 15
    exercito += 10
    estabilidade -= 2
    print("Exército fortalecido.")
    return economia, exercito, estabilidade


def aumentar_impostos(economia, estabilidade):
    economia += 25
    estabilidade -= 15
    print("Impostos aumentados.")
    return economia, estabilidade


def atacar(exercito, economia, estabilidade):

    paises = {
        1: 30,
        2: 60,
        3: 100
    }

    print("\n1 - País fraco")
    print("2 - País médio")
    print("3 - País forte")

    alvo = int(input("Escolha o alvo: "))

    if alvo not in paises:
        print("Alvo inválido.")
        return False, exercito, economia, estabilidade

    forca_inimiga = paises[alvo]

    chance_vitoria = exercito / (exercito + forca_inimiga)

    if random.random() < chance_vitoria:
        print("\nVitória na guerra!")
        economia += 50
        perda = int(forca_inimiga * 0.3)
        exercito -= perda
        estabilidade -= 5
        print(f"Perdeu {perda} soldados.")
        return False, exercito, economia, estabilidade

    else:
        print("\nDerrota devastadora...")
        estabilidade -= 30
        return True, exercito, economia, estabilidade


def passar_ano(ano, economia, populacao, estabilidade):
    ano += 1

    crescimento_pop = int(populacao * 0.01)
    populacao += crescimento_pop

    economia += int(populacao * 0.02)

    if estabilidade < 30:
        economia -= 15
        print("Crise interna afetou a economia.")

    return ano, economia, populacao


# ===== LOOP PRINCIPAL =====

while jogando:

    mostrar_status(ano, economia, exercito, populacao, estabilidade)

    print("\nO que deseja fazer?")
    print("1 - Investir na Economia")
    print("2 - Investir no Exército")
    print("3 - Aumentar Impostos")
    print("4 - Atacar")
    print("5 - Passar Ano")
    print("6 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        economia, estabilidade = investir_economia(economia, estabilidade)

    elif escolha == "2":
        economia, exercito, estabilidade = investir_exercito(
            economia, exercito, estabilidade
        )

    elif escolha == "3":
        economia, estabilidade = aumentar_impostos(economia, estabilidade)

    elif escolha == "4":
        perdeu, exercito, economia, estabilidade = atacar(
            exercito, economia, estabilidade
        )
        if perdeu:
            print("Seu governo foi destruído.")
            jogando = False

    elif escolha == "5":
        print("O ano passou...")

    elif escolha == "6":
        print("Encerrando governo...")
        jogando = False

    else:
        print("Opção inválida.")

    if not jogando:
        break

    # PASSA O ANO AUTOMATICAMENTE
    ano, economia, populacao = passar_ano(
        ano, economia, populacao, estabilidade
    )

    # CONDIÇÕES DE COLAPSO
    if estabilidade <= 10:
        print("\nGuerra civil começou. Governo caiu.")
        jogando = False

    if economia <= 0:
        print("\nO país faliu. Você foi deposto.")
        jogando = False

    if exercito <= 0:
        print("\nSem exército. O país foi invadido.")
        jogando = False

    input("\nPressione ENTER para continuar...")
    limpar_tela()

print("\n=== FIM DE JOGO ===")