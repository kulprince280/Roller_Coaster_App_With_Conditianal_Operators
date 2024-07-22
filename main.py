height = int( input("What is your height in cm? "))
age = int(input("How old are you? "))
if height > 120:
  print("Can ride")
  if  age < 12:
    print("$5")
  elif  age < 18:
    print("$7")
  else:
    print("$12")
else:
 print("Can't ride")
 
   