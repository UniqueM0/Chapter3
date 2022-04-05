
# i = 0 # iterator / incrementor
# while i < 10:
#     print("Hello World!" + str(i))
#     i = i +1  #i = i + 1



# num = 0 
# while num <= 5:
#     print("Hello world! " + str(num))
#     num += 1


## Movie Quotations
# print("This program displays a famous movie quotation.")
# responses = ('1', '2', '3')
# response = '0'
# while response not in responses:
#     response = input("Enter 1, 2,  or, 3: ")
#     if response == '1':
#         print("Plastics.")
#     elif response == '2':
#         print("Rosebud.")
#     elif response == '3':
#         print("That's all folks.")





# print("This program displays a famous movie quotation.")

# resps = ("1", "2", "3")
# resp = "0"

# while resp not in resps:
#     resp = input("Enter 1, 2 or 3: ")
#     if resp == "1":
#         print("Plastic.")
#     elif resp == "2":
#         print("Rosebud.")
#     elif resp == "3":
#         print("That's all folks.")



## Find the minimum, maximum and average of a sequence of numbers.
# count = 0 
# total = 0

# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number:"))
# min = num
# max = num

# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval(input("Enter a nonnegative number: "))

# if count > 0:
#     print("Min: ", str(min))
#     print("Max: ", str(max))
#     print("Average: ", str(total / count))
# else:
#     print("No nonnegative numbers were entered2")







# ## Find the minimum, maximum and average of a sequence of numbers.
# count = 0 
# numbers = []
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number:"))
# numbers.append(num)
# while num != -1:
#     count += 1
#     num = eval("Enter a nonnegative number: ")
# if count > 0:
#     print("Min: ", str(min))
#     print("Max: ", str(max))
#     print("Average: ", str(total / count))
# else:
#     print("No nonnegative numbers were entered2")   




# list1 = [300, 1, 2, 3, 60]
# list1.sort()
# list1[0]
# list1[-1]




# i = 0
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 100000:
#     balance += rate * balance 
#     i +=1
# print("In ", str(i), "years you will have a million dollars")



list1 = []
while True:
    num = eval(input("Enter a nonnegative number: "))
    if num == -1:
        break
    list1.append(num)

print(list1)
