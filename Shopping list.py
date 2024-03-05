#Shopping list
import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

foods = ["Meat","Cheese"]
print("Welcome to the shopping list")
print("Current Date and Time:" + month + "/" + day + "\t" + hour + ":" + minute )
print("You currently have" + foods[0] + "and" + foods[1] + "in your list.")

#get user input 
food = input("\nType of food to add to the shopping list: ")
foods.append(food.title())
food = input("\nType of food to add to the shopping list: ")
foods.append(food.title())
food = input("\nType of food to add to the shopping list: ")
foods.append(food.title())

#Print and sort list
print("\nHere is your shopping list: ")
print(foods)
foods.sort()
print("Here is your Shopping list sorted: ")
print(foods)

print("\nSimulating Shopping list...")
print("\nCurrent Shopping list: " + str(len(foods)) + "Items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + "from the list...")
print("\nSimulating Shopping list...")
print("\nCurrent Shopping list: " + str(len(foods)) + "Items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + "from the list...")
print("\nSimulating Shopping list...")
print("\nCurrent Shopping list: " + str(len(foods)) + "Items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + "from the list...")

#shop is out of item
print("\nCurrent Shopping list: " + str(len(foods)) + "items")
print(foods)
no_item = foods.pop ()
print("\nSorry, the shop is out of " + no_item + ".")
new_food = input("what food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remains on your Shopping list:")
print(foods)