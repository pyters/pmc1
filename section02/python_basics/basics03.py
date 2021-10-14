with open('file.txt','a+') as a:
    a.seek(0)
    a.write('\n' + a.read())