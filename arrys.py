 # arrays declaration  ( using  repeatitive)

hotels = [] #this is empty array

hotels.append("sheraton")
hotels.append("mandho")
hotels.append("Abera")
hotels.append("Chala")
hotels.append("Ware")

# print(hotels)

    # using for loop
for i in  range(0,5):
    hotels_input = input('enter the hotel name:')
    hotels.append(hotels_input)

# print(hotels)

user_input = input("Enter values separated by commas: ")
#splitting the input  into a list
input_values = user_input.split(",")
result_array =[]

#loop through the input values and append to the array
for values in input_values:
    #strip any extra whitespace and append to the result array 

    result_array.append(values.strip())

#output the result_array
print(result_array)
  

