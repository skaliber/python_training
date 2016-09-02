import re


def split_the_string():
    mystr = "this is a string with words"
    wordlist = re.sub("[^\w]", " ",  mystr).split()
    print(wordlist)
