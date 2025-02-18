def createArray():
    #Aarray searching and // other explain 
    #  def arrayCreation():
    numbers = []
    #Accet the value collection from users 
    user_input =input("Enter the number Separeted")
    input_values = user_input.split(",")
    for values in input_values:
        numbers.append(int(values.strip()))
    print(numbers)
    return numbers  # it returns array that has been createted 
 #Initialize index and boolean flag 
 #  
def arraySearching(number,arrayName):
    index =0
    found = False
    #  while loop condition based on the boolean value found 
    while index < len(arrayName) and not found:
        if arrayName [index] == number:
            found =True   #Set found to true if the target 
        index +=1  # move to the netx index 

    return found 


numbers_array = createArray()
target_value = int(input("Enter the target value to search: "))

if arraySearching(target_value, numbers_array):
    print(f"value{target_value}found in the target array.")
else:
    print(f"value{target_value}not found in the target array. ")

 

# def addTwoNumbers(numberOne, numberTwo):
#     return numberOne + numberTwo

# def arrayCreation():
#     numbers = []
#     user_input = input("Enter the numbers separated by commas: ")
#     input_values = user_input.split(",")
#     for value in input_values:
#         numbers.append(int(value.strip()))
#     print(numbers)
#     return numbers  # it returns array that has been created

# def arraySearching(target, arrayName):
#     index = 0
#     found = False
#     while index < len(arrayName) and not found:
#         if arrayName[index] == target:
#             found = True  # Set found to true if the target is found
#         index += 1  # move to the next index
#     return found

# # Main function
# numbers_array = arrayCreation()
# target_value = int(input("Enter the target value to search: "))
# if arraySearching(target_value, numbers_array):
#     print(f"value {target_value} found in the array.")
# else:
#     print(f"value {target_value} not found in the array.")