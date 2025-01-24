       # i`m trying to the accet the four number`
number_one = int(input("insert the first number"))
number_twoe = int(input("insert the second number"))
number_three = int(input("insert the third number"))
number_for = int(input("insert the fourth number"))

choice =input("enter your preferd calculation: average, multiply or sum")

        # calculate average

average =(number_one + number_twoe + number_three + number_for )/4

      # calculate sum
sum = (number_one + number_twoe + number_three + number_for)
    # calculate the multiplication
multiplication = (number_one * number_twoe * number_three * number_for)
# display the result baseed on condition /choice
if(choice == "average"):
    print("the average of number is: ",average)
elif(choice == "sum"):
   print("the sum of number is : ",sum)
elif(choice == "multiplication"):
   print(choice == "the multiplication of number is : ", multiplication )

else:
   print(average, sum , multiplication)