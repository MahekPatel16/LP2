def calculator():
  print("Enter 2 numbers: ")
  num1 = int(input("Enter 1st number: "))
  num2 = int(input("Enter 2nd number: "))
  print("Enter the number for the task to be performed: ")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    sum = num1+num2
    print("Addition",sum)
  elif choice == 2:
    if num1>num2:
      diff = num1 - num2
      print("Difference: ",diff)
    else:
      diff = num2-num1
      print("Difference: ",diff)
  elif choice == 3:
    product = num1 * num2
    print("Product: ",product)
  else:
    div = num1/num2
    print("Division: ",div)

calculator()


  
