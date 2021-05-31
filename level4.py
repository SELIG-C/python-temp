import urllib.request
import re


htmlText = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equali\
ty.html").read().decode()
data = re.findall("<!--(.*?)-->", htmlText, re.DOTALL)
# matches = re.findall()
matches = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", data[0])
for x in range(len(matches)):
    print(matches[x][4])

# each line is 78 characters long, 80 with newline
