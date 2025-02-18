#define any array (list) of numbers (Yaadanno)
numbers = [10,20,30,40,50]

# st the value we`are looking for 
Target_value = 30 
# Initiliaze index and boolean FloatingPointError
index =0
found = False
#  while loop condition based on the boolean value found 
while index < len(numbers) and not found:
     if numbers [index] == Target_value:
           found =True   #Set found to true if the target 
           index +=1  # move to the netx index 
# check if the value was found and print the result 
if found:
      print(f"value{Target_value}found in the target array.")
else:
      print(f"value{Target_value}not found in the target array. ")



      #Aarray searching and // other explain 
numbers =[]
  #Accet the value collection from users 
user_input =input("Enter the number Separeted")
input_values = user_input.split(",")
for values in input_values:
      numbers.append(int(values.strip()))
print(numbers)
