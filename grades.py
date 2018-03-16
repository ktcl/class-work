#Exercise 3.3
try:
    x = float(input("Enter a score between 0.0 and 1.0: "))
    if x >= 0.0 and x <= 1.0:
        pass
    else:
        print("Error: Number must be a value between 0.0 and 1.0.")
        quit()

except:
    print("Error: Must enter a number.")
    quit()
if x >= 0.9:
    print('A')
elif x >= 0.8:
    print('B')
elif x >= 0.7:
    print('C')
elif x >= 0.6:
    print('D')
elif x < 0.6:
    print ('F')

quit()

    

