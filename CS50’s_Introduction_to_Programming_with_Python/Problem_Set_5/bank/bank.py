def main():
    #Pede um cumprimento.
    g = input("Give me a greeting!")

    v = value(g)
    print(v)

def value(greeting):
    greeting = greeting.strip().lower()

    #Retornos diferentes, dependendo do cumprimento.
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


# Garante que a função main só seja executada quando o arquivo for rodado diretamente.
if __name__ == "__main__":
    main()
