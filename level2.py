def parser(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    shiftedAlphabets = alphabets[2:len(string)] + alphabets[0:2]
    print(shiftedAlphabets)
    table = string.maketrans(alphabets, shiftedAlphabets)
    return string.translate(table)


print(parser("http://www.pythonchallenge.com/pc/def/map.html"))
