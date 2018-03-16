#Exercise 7 Line Count in Text File
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)