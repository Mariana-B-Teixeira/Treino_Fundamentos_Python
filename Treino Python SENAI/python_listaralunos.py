alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso: ")
    aluno = {"nome": nome, "curso": curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i, aluno in enumerate(alunos):
            print(f"{i+1}. {aluno['nome']} - {aluno['curso']}")

def remover_aluno():
    listar_alunos()
    numero = (int(input("Digite o número do aluno para remover: ")))
    alunos.pop(numero - 1)
    print("Aluno removido!")

while True:
    print("\n1. Cadastrar")
    print("2. Listar")
    print("3. Remover")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        remover_aluno()
    elif opcao == "4":
        break