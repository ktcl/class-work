#Exercise 7 Line Count in Text File
fname = input("Enter the file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line.find('From:') == -1: continue
    print(line)