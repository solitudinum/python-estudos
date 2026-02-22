alunos = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


def mostrar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
        return
    
    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Nota:", aluno["nota"])
        print("------------------")
    print()


def calcular_media():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
        return
    
    soma = 0
    
    for aluno in alunos:
        soma += aluno["nota"]
    
    media = soma / len(alunos)
    print("Média da turma:", media, "\n")


# Menu principal
while True:
    print("1 - Cadastrar aluno")
    print("2 - Mostrar alunos")
    print("3 - Calcular média")
    print("4 - Sair")
    
    escolha = input("Escolha: ")
    
    if escolha == "1":
        cadastrar_aluno()
        
    elif escolha == "2":
        mostrar_alunos()
        
    elif escolha == "3":
        calcular_media()
        
    elif escolha == "4":
        print("Encerrando sistema...")
        break
        
    else:
        print("Opção inválida.\n")