#Exercise 7 Line Count in Text File
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)