fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

with open(fname, "r", encoding="UTF8") as fh :
    count = 0
    lst = []
    for line in fh :
        if not line.startswith("From") :
            continue
        if line.startswith("From:") :
            continue
        line = line.rstrip()
        ls = line.split()
        count += 1
        print(ls[1])

print("There were", count, "lines in the file with From as the first word")
