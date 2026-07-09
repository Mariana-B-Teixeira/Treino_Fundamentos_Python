def main():
    nome = str(input(""))
    print(replace(nome))

def replace(x):
    x = x.replace(' ', '...')
    return x

main()


