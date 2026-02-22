import random 
import os 
nome = input("Qual o nome do personagem?  ")
vida = 100
ouro = 0
ataque = 15
defesa = 5
jogando = True
vida_maxima = 100

vida_inimigo = 50
ataque_inimigo = 20

xp = 0
level = 1
xp_nec = 50
base_ataque = 10
ataque = base_ataque

fase = 1

def atacar():
    return 15

def sofrer(ataque_inimigo):
    return ataque_inimigo
     
def limpar_tela():
     os.system("cls") 


def mostrar_status(vida, ouro, nome, ataque, defesa, fase):
        print("\n======= STATUS DO PERSONAGEM  =======")
        print(f"Nome: {nome}")
        print(f"Vida: {vida}")
        print(f"Ouro: {ouro}")
        print(f"Ataque: {ataque}")
        print(f"Defesa: {defesa}")
        print(f"Fase: {fase}")
        print("===============================")


def mostrar_vida(vida, vida_maxima):
    porcentagem = vida / vida_maxima
    blocos = int(porcentagem * 10)
    barra = "⬜" * blocos + "_" * (10 - blocos)
    print(f"Vida:  [{barra}]")



def loja(ataque, defesa, ouro):
   print("----------- LOJA ABERTA ---------")
   print("1 - Comprar escudo- +10 defesa, -50 ouro")
   print("2-  - Comprar espada- +20 ataque, -50 ouro")
   print("3- Seguir caminho..")

     #Criou o jogador

     #Criou o inimigo

jogando = True
     #fazer batalha:

# ===== LOOP PRINCIPAL =====
while jogando:
       mostrar_status(vida, ouro, nome, ataque, defesa, fase)
       print("--------------------")
       

       escolha = input("Você encontrou um bandido. \n ---- Escolha:----- \n 1-Fugir-- \n 2- Enfrentar--  \n ----------- : ")
       if escolha == "1":
        print("Você fugiu... ")
       jogando = False

       if escolha == "2":
        while vida >0 and vida_inimigo > 0:
        #jogador ataca

         dano_jogador = random.randint(10, ataque)
         vida_inimigo -= dano_jogador
         print(f"Você causou {dano_jogador} de dano!")
       if vida_inimigo <= 0:
          vida_inimigo = 0
          jogando = False
    
    #inimigo ataca
          dano_inimigo = random.randint(5, ataque_inimigo)
          vida -= dano_inimigo - defesa
          print(f"O bandido tentou te causar {dano_inimigo} de dano em você! ")
          print(f"- {defesa} de dano, Seu escudo bloqueou!")
          print(f"Sua vida: {vida}")
          mostrar_vida(vida, vida_maxima)
          print(f"Vida do bandido: {vida_inimigo} ")
          print("----------------------")
          if vida_inimigo <= 0:
           print("O bandido  fugiu! \n------------ \n Você ganhou! \n ------------ \n+ 10 de Ouro!")
           xp += 50
           ouro += 50
           print(f"Mais {xp} de XP!")
    

           while xp >= xp_nec:
             level += 1
             vida_maxima += 20
             defesa += 10
             vida = vida_maxima
             xp -= xp_nec
             ataque = base_ataque + (level * 3)
             xp_nec = level * 50
             fase += 1
             print(f"Você upou de level! Level {level}")

             input("Pressione Enter para continuar:")
             limpar_tela()
             jogando = False
print("\n----------  Proxima etapa --------")
mostrar_status(vida, ouro, nome, ataque, defesa, fase)
print("--------------------")




loja(ataque, defesa, ouro)
escolha = input("Escolha:")
if  escolha == "1":
    defesa += 10
    ouro -= 50
    print("Você comprou um escudo! Atributos aprimorados.")

elif escolha == "2":
            ataque += 20
            ouro -= 50
            print("Você comprou uma espada! Atributos aprimorados.")
elif escolha == "3":
    print("Você não comprou nada..")


mundo = input("-----------------\n Você está andando pela floresta até que acha uma caverna, o que vc faz?\n 1- Entra na caverna: \n--------- \n  2- Segue caminho e vai para casa:\n  Escolha:   ")
if mundo == "2":
    print("Você chegou em casa..sem graça")
    jogando = False
    
if mundo == "1":
    print("Ao entrar vc cai num buraco e chega em outro mundo.\n--------------\n Vc está andando e se depara com uma criatura estranha\n O que será que é??")
    inimigo2 = random.randint(1, 2)
    if inimigo2 == 1:
            print("É um goblin!!")
            escolha = input("\n ------------\n O que vc faz? 1- Corre ----- 2- Enfrenta ele \n Escolha:")
            if escolha == "1":
              print("Ele te alcançou e te matou. Fim de jogo!")
            if escolha == "2":
             vida_inimigo = 100
             while vida >0 and vida_inimigo > 0:
              dano_jogador = random.randint(10, ataque)
              vida_inimigo -= dano_jogador
              print(f"Você causou {dano_jogador} de dano!")
            if vida_inimigo <= 0:
               vida_inimigo = 0
               jogando = False

               dano_inimigo = random.randint(5, ataque_inimigo)
               vida -= dano_inimigo - defesa
               print(f"O bandido tentou te causar {dano_inimigo} de dano em você! ")
               print(f"- {defesa} de dano, Seu escudo bloqueou!")
               print(f"Sua vida: {vida}")
               mostrar_vida(vida, vida_maxima)
               print(f"Vida do inimigo: {vida_inimigo} ")
               print("----------------------")
               if vida_inimigo <= 0:
                print("O inimigo  fugiu! \n------------ \n Você ganhou! \n ------------ \n+ 10 de Ouro!")
               xp += 50
               ouro += 50
               print(f"Mais {xp} de XP!")

    if inimigo2 == 2:
      print("É um Anão malvado!!")
      escolha = input("\n ------------\n O que vc faz? 1- Corre ----- 2- Enfrenta ele \n Escolha:")
      if escolha == "1":
       print("Ele te alcançou e te matou. Fim de jogo!")
       if escolha == "2":
        vida_inimigo = 100
        while vida >0 and vida_inimigo > 0:
         dano_jogador = random.randint(10, ataque)
         vida_inimigo -= dano_jogador
         print(f"Você causou {dano_jogador} de dano!")
        if vida_inimigo <= 0:
         vida_inimigo = 0
         jogando = False

         dano_inimigo = random.randint(5, ataque_inimigo)
         vida -= dano_inimigo - defesa
         print(f"O bandido tentou te causar {dano_inimigo} de dano em você! ")
         print(f"- {defesa} de dano, Seu escudo bloqueou!")
         print(f"Sua vida: {vida}")
         mostrar_vida(vida, vida_maxima)
         print(f"Vida do inimigo: {vida_inimigo} ")
         print("----------------------")
         if vida_inimigo <= 0:
          print("O inimigo  fugiu! \n------------ \n Você ganhou! \n ------------ \n+ 10 de Ouro!")
          xp += 50
          ouro += 50
          print(f"Mais {xp} de XP!")
