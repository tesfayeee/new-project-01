
# A1 --while loop = non stop statement

# number_one=int(input("insert the number"))
# number_two=int(input("insert the number"))
# number_three=int(input("insert the number"))
# number_four=int(input("insert the number"))
# number_five=int(input("insert the number"))

# print("inseert the number ")



# # A2-- array statement
numbers = []  # array the collection of deta 
counter = 0
while counter < 4:
  number_input = int(input("Entery the number"))
  numbers.append(number_input)
  counter = counter+1




#   # A3-- accept the preference of our course 

choice  = input("inter your preference calculaton ;sum; avarage; or multiply "    )
  #calculate the sum of numbers
sum = numbers[0]+numbers[1]+numbers[2]+numbers[3]
average =sum/4
  #calculated the multiplication of the numbers

multiple = numbers[0] * numbers[1] * numbers[2] * numbers[3]

#     #A4-- display the calculation the user choce 

if (choice == 'sum'):
    print("the sum of number ",sum)
elif (choice == 'average'):
   print("the average of number ",average)
elif (choice == 'multiply'): 
 print("the multiply of number ", multiple)
else:
 print(sum, multiple,average)
