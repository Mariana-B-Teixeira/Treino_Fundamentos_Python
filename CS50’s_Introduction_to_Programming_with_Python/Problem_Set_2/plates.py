def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_part = ""
    second_part = ""
    bool = True
    c = 0

    for x in s:
        c = c + 1

    if c < 2 or c > 6:
        bool = False


    if s[0:1].isdigit():
        bool = False

    for y in s[2:]:
        if y.isdigit():
            if y == "0":
                bool = False

            else:
                index = s.index(y)
                first_part, second_part = s[:index], s[index:]
                break

    for y in second_part:
        if y.isdigit():
            continue
        else:
            bool = False

    return bool

main()
