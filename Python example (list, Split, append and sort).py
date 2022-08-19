with open("romeo.txt", "r", encoding="UTF8") as fh :
    lst = list()
    for line in fh :
        line = line.rstrip()
        ls = line.split()
        for word in ls :
            if not word in lst :
                lst.append(word)
    lst.sort()
    print(lst)
