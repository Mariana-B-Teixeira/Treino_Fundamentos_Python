def main():
    mass = int(input('m: '))
    print('E: ', Joules(mass), sep="")

def Joules(m):
    E = m*300000000**2
    return E

main()
