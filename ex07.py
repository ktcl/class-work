#Exercise 7 Line Count in Text File
xfile = open('mbox-short.txt')
count = 0
for line in xfile:
    count = count + 1
print('Line Count: ',count)