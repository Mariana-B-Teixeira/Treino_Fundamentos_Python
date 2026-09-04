def main():
    palavra = input("Input: ")
    palavra.strip()
    palavra = shorten(palavra)
    if palavra != "":
        print("Output: ", palavra, sep="")

    else:
        print("Write a word!")

def shorten(word):
    X = ""
    for v in word:
        if (v=="a") or (v=="A") or (v=="e") or (v=="E") or (v=="i") or (v=="I") or (v=="o") or (v=="O")or (v=="u") or (v=="U"):
            continue
        else:
            X += v
    return X

if __name__ == "__main__":
    main()
