#Exercise 7.2 Spam Confidence Calculation
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count=0
total=0.0
for line in fhand:
    line  = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        piece = float(line[20:])
        count = count + 1
        total = total + piece
print('Average Spam Confidence: ', total/count)