fruits = ["Apples", "Bananas", "Grapes", "Oranges"]
vegetables = ["Mushrooms", "Tomatoes", "Potatoes", "Broccoli"]

vegetables[2:3] = "Cherry Tomatoes", "Sweet Potatoes"
vegetables.append("Spinach")

grocery_list = fruits + vegetables
grocery_list.append("Bread")
# print(grocery_list)
# # print(len(grocery_list))
# grocery_list[2] = "Blueberries"
# print(grocery_list)

grocery_list2 = [fruits, vegetables]
print(grocery_list2)
grocery_list2[0][2] = "Blackberries"
print(grocery_list2)
# print(len(grocery_list2))


sweet_fruits = ["Apple", "Watermelon", "Mango"]
sour_fruits = ["Oranges", "Gooseberry"]
fruits = [sweet_fruits, sour_fruits]

vegetables = ["Egg Plant", "Leek"]

grocery_list = [fruits, vegetables]

print(grocery_list)

sweet_fruits[1] = "Pear"
# grocery_list[0][0][1] = "Pear"

print(grocery_list)


a = 10

if a < 5:
  print('Boo boo')
elif a < 10:
  print('Boo')
elif a > 10:
  print('Hurray')
else:
  print('Bingo!')


a = 7fruits = ["Apples", "Bananas", "Grapes", "Oranges"]
vegetables = ["Mushrooms", "Tomatoes", "Potatoes", "Broccoli"]

vegetables[2:3] = "Cherry Tomatoes", "Sweet Potatoes"
vegetables.append("Spinach")

grocery_list = fruits + vegetables
grocery_list.append("Bread")
# print(grocery_list)
# # print(len(grocery_list))
# grocery_list[2] = "Blueberries"
# print(grocery_list)

grocery_list2 = [fruits, vegetables]
print(grocery_list2)
grocery_list2[0][2] = "Blackberries"
print(grocery_list2)
# print(len(grocery_list2))


sweet_fruits = ["Apple", "Watermelon", "Mango"]
sour_fruits = ["Oranges", "Gooseberry"]
fruits = [sweet_fruits, sour_fruits]

vegetables = ["Egg Plant", "Leek"]

grocery_list = [fruits, vegetables]

print(grocery_list)

sweet_fruits[1] = "Pear"
# grocery_list[0][0][1] = "Pear"

print(grocery_list)


a = 10

if a < 5:
  print('Boo boo')
elif a < 10:
  print('Boo')
elif a > 10:
  print('Hurray')
else:
  print('Bingo!')


a = 6

# if a ==\2 % 0       
# print("true")                                                 
if a % 2 == 0:
  print(f"{a} is an even number")
else: 
  print(f"{a} is an odd number")

# If money > 1 billion say "Billionaire"
# > 1 million "Millionaire"
# > 100K "Upper middle class"
# > 10K "Middle class"
# Otherwise "Sorry!"

money = 100

if money >= 1000000000:
  print("Billionaire")
elif money >= 1000000:
  print("millionaire")
elif money >= 100000:
  print("Upper middle class")
elif money >= 10000:
  print("middle class")  
else:
  print("sorry")

# if a ==\2 % 0       
# print("true")                                                 
if a % 2 == 0:
  print(f"{a} is an even number")
else: 
  print(f"{a} is an odd number")

# If money > 1 billion say "Billionaire"
# > 1 million "Millionaire"
# > 100K "Upper middle class"
# > 10K "Middle class"
# Otherwise "Sorry!"

money = 100

if money >= 1000000000:
  print("Billionaire")
elif money >= 1000000:
  print("millionaire")
elif money >= 100000:
  print("Upper middle class")
elif money >= 10000:
  print("middle class")  
else:
  print("sorry")