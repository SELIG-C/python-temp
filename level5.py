import urllib.request
import re
currentNothing = "89879"


def nextNothingGetter(number):
    urlString = "http://www.pythonchallenge.com/pc/def/\
linkedlist.php?nothing=" + str(number)
    data = urllib.request.urlopen(urlString).read().decode()
    # print(re.findall("[0-9]+", data))
    return re.findall("[0-9]+$", data)[0]


for x in range(400):
    try:
        currentNothing = nextNothingGetter(currentNothing)
        print(currentNothing)
    except:
        print("error!")
        break
