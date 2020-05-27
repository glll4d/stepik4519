from urllib.request import urlopen
import re
from collections import Counter


html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("UTF-8")
regex = '<code>(.*?)</code>'
found = sorted(re.findall(regex, html))
print(Counter(found).most_common())
