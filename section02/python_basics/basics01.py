
main_list = []
while True:
    a = input("enter a phrase: ")
    if a == "\end":
        break
    else:
        main_list.append(a)
        continue

ms = ""
for word in main_list:
    ms = ms + word[0].upper() + word[1:] + '. ';

print(ms)