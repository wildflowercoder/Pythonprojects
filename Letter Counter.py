print("Welcome to the Letter Counter App")

#Get user input

name = input("\nWhat is your name: ").title().strip()
print("Hello,  " + name + "!")

print("I will count the number of times that a specific letter occurs in a message:")
message = input("\nPlease enter a message:")
letter = input("Which letter would you like to count the occurrences of:")

#Change to lower case

message = message.lower()
letter = letter.lower()


letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + "" + letter + "'s in it")