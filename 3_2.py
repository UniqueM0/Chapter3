
# grade = 90

# condition = grade >=90

# if condition:
#     # execute when true
#     print("your grade is A")
# else:
#     # execute when false
#     print("your grade is not A")

# ## Determine the larger of two numbers
# ## Obtain the two numbers from the user

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# try:

# # Determine and display the larger value

# # if num1 > num2:
# #     larger_value = num1 #execute this statement if the condition is true
# # else:
# #     larger_value = num2 # execute this statement if the condition is false
# # print("The larger value is", str(larger_value) + ".")

# # print(isinstance(num1, str)) #will print false

# # if isinstance(num1, str):
# #     print("Data type not allowed: Please specify a numeric data type")


# print("1", isinstance(num1, str))
# print("2", isinstance(num2, str))

# if isinstance(num1, str) or isinstance(num2, str):
#     print ("Data type not allowed: please specify a numeric data")
# else:
#     num1 = eval(num1)
#     num2 = eval(num2)
#     if num1 > num2:
#         larger_val = num1
#     else: 
#         larger_val = num2
#     print("The larger value is " + str(larger_val))
# except:
#     print("Data is not allowed")


# answer = eval(input("How many gallons does a ten-gallon hat hold? "))

# if (0.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")
# print("It hold about 3/4 of a gallon.")


## Evaluate profit
# Obtain input from user
from asyncio import constants


# cost = eval(input("Enter total costs: "))
# revenu = eval(input("Enter total reveune: "))
# #Determine and display profit or loss
# if cost == revenue:
#     print = ("Break even")
# result = "is "
#     result 
#     if profit < 0:
#         result = "loss" + result 
#     else: 
#         result = "Profit" + result 



# ## Determine the larger of two numbers
# # Obtain the two numbers from the user
# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# # Determine and display the larger value
# if num1 > num2:
#     print("The larger value is", str(num1) + ".")
# elif num2 > num1:
#     print("The larger value is", str(num2) + ".")
# # else:
# #     print("The two values are equal. ")



# ## Bestow graduation honors.
# # # Request grade point average
# # gpa = eval(input("Enter your gpa: "))
# # #Determine if honors are warranted
# # if gpa >= 3.9:
# #     honors = "summa cum laude."
# # elif gpa >= 3.6:
# #     honors = "magna cum laude."
# # elif gpa >= 3.3:
# #     honors = "cum laude."
# # else:
# #     honors = "."
# # #display conclusion
# # print("You graduated " + honors)


# ## Request two numbers and find their sum. Validate the input
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# #Display sum if enteries are valid. Otherwise, inform the user where invalid enteries were made
# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     else:
#             print("The first entery was not a proper number.")
# else:
#         print("The second entry was not a proper number.")


# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#      print("The first entery was not a proper number.")
#   print("The second entry was not a proper number.")



if 7:
    print("A nonzero number is true.")
else:
    print("The number zero is false.")
if []:
    print("A nonempty list is true.")
else:
    print("An empty list is false.")
if ["spam"]:
    print("A nonempty list is true.")
else:
    print("The empty list is false.")




