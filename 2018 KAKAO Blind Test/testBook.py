import re






str1 = "23242412 4 1 A BCDE 1 2 3 1241"
str1 = re.sub('[^ 0-9]', '', str1)
print(str1)



String = 'HELLO WORLD'
for s in String:
    print(s)