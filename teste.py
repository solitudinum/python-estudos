pecados = []

def guardar():
    pecado = input("Qual seu pecado (s): \n")


    pessoa = {
     "pecados" :  pecado

     }
    
    pecados.append(pessoa)
    print("Registrado. \n")


def  mostrar():
    if len(pecados) == 0:
            print("Nenhum pecado registrado.")
            return
    for pessoa in pecados:
            print("Pecado (s): ", pessoa["pecados"], "\n" )


#menu principal
while True:
    print("1 - Cadastrar pecados ")
    print("2 - sair")
    print("3 - Mostrar pecados")
    escolha = input("Escolha: ")

    if escolha == "1":
        guardar()
    
    elif escolha == "2":
        print("\n Você saiu..")
        break

    elif escolha == "3":
        mostrar()

    else:
        print("Opção inválida..\n")
