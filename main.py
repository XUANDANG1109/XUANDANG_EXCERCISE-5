# Name: Xuan Dang

# Phase 1
import random
number = int(input("Input dice to roll:"))
sum = 0
for i in range (number):
    sum = random.randint(1,6)
    sum += sum
print("The sum of the numbers:", sum)

# Phase 2
list = []
number = input("Enter the number(input an empty string to quit):")

while number != "":
    list.append(number)
    number = input("Enter the number(input an empty string to quit):")
list.sort(reverse=True)
print("5 greatest numbers are:")
for i in range (5):
    print(list[i])

# Phase 3
number = int(input("Enter a number:"))
if number == 0 or number <= 1:
    print("This is not a prime number")
else:
    for i in range(2,number):
        if number % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")

# Phase 4
list_city = []
print ("Enter the names of five cities:")

for i in range (5):
    name_city = input("Name of a city:")
    list_city.append(name_city)
for i in list_city:
    print(list_city)







