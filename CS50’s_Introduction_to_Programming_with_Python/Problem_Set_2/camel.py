def main():
    camel = input("camelCase: ")
    snake = print(snake_case(camel))


def snake_case(c):

    s = ""
    for char in c:

        if char.isupper():
            s += "_" + char.lower()
        else:
            s+= char

    if s.startswith("_"):
        s = s[1:]

    return s

main()
