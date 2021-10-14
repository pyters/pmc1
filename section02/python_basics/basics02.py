def count(ch, path):
    with open(path,'r') as myfile:
        content = myfile.read()
    #out = [k for k in content if k==ch]
    return content.count(ch)

print(count('a','fruits.txt'))

    