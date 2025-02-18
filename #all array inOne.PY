#all array inOne
# Define an array


# A1 Define an array
numbers = [1, 2, 3, 4, 5]

# A2 Initialize index
index = 0

# A3 Use a while loop to iterate through the array
while index < len(numbers):
    number = numbers[index]
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    index += 1


# # A4 Define a function to check if numbers are even or odd
# def check_even_odd(arr):
#     for number in arr:
#         if number % 2 == 0:
#             print(f"{number} is even")
#         else:
#             print(f"{number} is odd")

# #A5 Define an array
# numbers = [1, 2, 3, 4, 5]

# #A6 Call the function with the array
# check_even_odd(numbers)
