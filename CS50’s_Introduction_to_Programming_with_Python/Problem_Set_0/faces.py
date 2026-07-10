def main():
    name = str(input(""))
    print(convert(name))

def convert(x):
    x = x.replace(':)', '🙂')
    x = x.replace(':(', '🙁')

    return x

main()
