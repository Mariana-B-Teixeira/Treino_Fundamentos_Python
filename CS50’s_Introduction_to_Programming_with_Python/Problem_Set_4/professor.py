# Testar biblioteca random
import random

def main():
    # Contagem de repostas
    i = 0

    # Pontuação
    score = 0

    # Nível de dificuldade
    Level = get_level()

    # 10 perguntas de adição básica
    while i < 10:

        # Números que fazem parte das operações aritméticas
        X = generate_integer(Level)
        Y = generate_integer(Level)

        # Resposta correta de cada operação
        soma = X + Y

        n = 0

        # 3 chances
        while n < 3:

            # Entrada da resposta do usuário
            answer = int(input(f"{X} + {Y} = "))

            # Correção da resposta do usuário (caso esteja errado)
            if answer != soma:
                print("EEE")
                n += 1
                continue

            # Correção da resposta do usuário (caso esteja correto)
            else:
                score += 1
                i += 1
                break

        # Correção da resposta do usuário (caso erre nas 3 chances)
        if n == 3:
            print(f"{X} + {Y} = {soma}")
            i += 1

    # Pontuação final do usuário, após 10 perguntas
    if i == 10:
        print(score)

# Função que recebe o nível de dificuldade
def get_level():
    while True:
        try:

            # Entrada da resposta do usuário quanto ao nível de dificuldade desejado
            Level = int(input("Level: "))

            # Restringe nível de dificuldade: de 1 a 3, se a resposta estiver fora do intervalo, repete pergunta
            if Level <= 0 or Level>3:
                raise ValueError
        except ValueError:
            continue

        except Exception as e:
            continue

        return Level

# Gera número de algarismos de acordo com nível de dificuldade
def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)

    elif level == 2:
        num = random.randint(10, 99)

    elif level == 3:
        num = random.randint(100, 999)

    return num

# Chama função de entrada main
if __name__ == "__main__":
    main()
