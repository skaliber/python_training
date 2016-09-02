def go() -> object:
    if 3 > 2:
        print("Test")

    print("please enter your prefference \n:")

    respose = input()

    if respose == "test".capitalize():
        print("yes please".swapcase())
    elif respose == "":
        print("you are so empty")
    else:
        print("no thank you".swapcase())
