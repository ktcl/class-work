#Exercise 3.2
try:
  hours = (float(input('Enter hours: ')))
except:
  print('Hours must be numeric.')
  quit()
  
try:
  rate = (float(input('Enter rate without $: ')))
except:
  print('Rate must be numeric.')
  quit()
  
pay = (hours*rate)+((hours-40)*(0.5*rate))
print()
print("Gross Pay: $",pay)