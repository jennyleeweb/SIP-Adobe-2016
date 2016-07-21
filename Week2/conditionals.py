number = 14
user_number = input("Guess my number: ")
while number != int(user_number):
	if int(user_number) < 14:
		print("Your number is too low")
		user_number = input("Try again: ")
	elif int(user_number) > 14:
		print("Your number is too high")
		user_number = input("Try again: ")
if int(user_number) == 14:
	print("You win! Game over")
    