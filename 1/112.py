from urllib.request import urlopen


html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode("UTF-8")
print("Python" if html.count("Python") > html.count("C++") else "C++")