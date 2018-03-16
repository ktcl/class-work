#Exercise 5.2
smallest = None
largest = None

while True:
    line = input('Enter Number: ')
    if line == 'done':
        break
    try:
        value = float(line)
    except:
        print('invalid entry')
        continue
    if smallest is None or value < smallest:
        smallest = value
    elif largest is None or value > largest:
        largest = value
Print('Max: ',largest)
Print('Min: ',smallest)


    

