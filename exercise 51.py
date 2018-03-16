#Exercise 5.1
count = 0
total = 0
while True:
    line = input('Enter Number: ')
    if line == 'done':
        break
    try:
        value = float(line)
    except:
        print('invalid entry')
        continue
    count=count+1
    total=total+value
print("Total: ",total)
print("Count: ",count)
print("Average: ",total/count)

    

