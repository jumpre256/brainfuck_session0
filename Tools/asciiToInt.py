


def main():

    while True:

        userInput = input("> ") #of ""char"" type.

        if ord(userInput[0]) != 8706:  #option+D.
            getCodesOfChars(userInput)
        else:
            break


def getCodesOfChars(value: str) -> None:
    codes = []
    for c in value:
        codes.append(ord(c))
    print(codes)


main()
