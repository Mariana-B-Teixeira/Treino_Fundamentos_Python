def main():
    palavra = input("Input: ")
    palavra.strip()
    palavra = vowels_omitted(palavra)
    print("Output: ", palavra, sep="")

def vowels_omitted(p):
    X = ""
    for v in p:
        if (v=="a") or (v=="A") or (v=="e") or (v=="E") or (v=="i") or (v=="I") or (v=="o") or (v=="O")or (v=="u") or (v=="U"):
            continue
        else:
            X += v
    return X

main()
