from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(html, 'html.parser')

cnt = 0
for a in soup.find_all('td'):
    cnt += int((a.get_text()))
print(cnt)
