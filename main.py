from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://naver.com')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("newfile.txt", 'w')
for anchor in soup.select("span"):
    data = str(i) + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()

f = open("C:/github/Face_Recognition/newfile.txt", 'w')
for i in range(1, 11):
    data = "%dth line .\n" % i
    f.write(data)
f.close(data)