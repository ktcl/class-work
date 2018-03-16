#Exercise 7.3 Easter Egg
fname = input("Enter the file name: ")
count = 0
try:
    fhand = open(fname)
except:
    if fname.lower() == "na na boo boo":
        print("na na boo boo - you've been punk'd") 
    else:
        print('File cannot be opened: ', fname)
    quit()
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print("There were ", count, "subject lines in ", fname)