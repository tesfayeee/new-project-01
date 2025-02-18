# create a function that computers the fuctorials  of Numbers
def fuctorialofNumbers(number):
 if(number == 0):
  return 1         
 else: #culculate the Factorials of the numbers by calling the function 
   return number * fuctorialofNumbers(number-1)
 
user_input = int(input("Enter the number: "))

result = fuctorialofNumbers(user_input)
print("the fuctorial of No", user_input, "is", result)

