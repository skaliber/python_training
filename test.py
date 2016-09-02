from operators import methods as meth


def main():
    meth.go()
    print("This only executes when %s is executed rather than imported" % __file__)

if __name__ == "__main__": main()


