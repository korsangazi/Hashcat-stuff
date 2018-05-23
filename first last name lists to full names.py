firstnames = [i.strip() for i in open("first names.txt", "r").readlines()]
lastnames = [i.strip() for i in open("last names.txt", "r").readlines()]


f = open("full names build.txt", "w")
for first in firstnames:
    for last in lastnames:
        f.write(first + " " + last + "\n")

f.close()
