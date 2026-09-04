def main():
    # Solicita ao usuário uma palavra ou frase.
    palavra = input("Input: ")
    palavra.strip()
    palavra = shorten(palavra)
    
    # Verifica se a palavra não está vazia e exibe o resultado formatado.
    if palavra != "":
        print("Output: ", palavra, sep="")

    else:
    # Se está vazia, pede por uma palavra.
        print("Write a word.")

def shorten(word):
    # Inicializa a variável que armazenará o texto sem as vogais
    X = ""
    
    # Percorre cada caractere da palavra e ignora as vogais (maiúsculas e minúsculas)
    for v in word:
        if (v=="a") or (v=="A") or (v=="e") or (v=="E") or (v=="i") or (v=="I") or (v=="o") or (v=="O")or (v=="u") or (v=="U"):
            continue
        else:
            X += v
            
    # Retorna o texto resultante sem as vogais.
    return X

# Garante que a função main só seja executada quando o arquivo for rodado diretamente.
if __name__ == "__main__":
    main()
