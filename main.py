# ATM Transactions

user = {'pin': 1234, 'balance': 10000}

def withdrawal():
	while True:
		amount = int(input("Enter the amount to withdraw: "))
		if amount > user['balance']:
			print("You do not have enough balance!")
		else:
			user['balance'] -= amount
			print(f"You have withdrawn ${amount}. Your balance is ${user['balance']}")
			break

def balance():
	print(f"Your balance is, ${user['balance']}" )

quit = False
print("Welcome to the ATM!")
max_attempts = 3
attempts = 0

while attempts < max_attempts:
	pin = int(input("Enter your four-digit pin: "))
	if pin == user['pin']:
		print("What do you want to do?\n")
		print("1. Withdrawal\n2. Balance\n3. Quit\n")
		choice = input()
		match choice:
			case "1": 
				withdrawal()
			case "2":
				balance()
			case "3":
				break
			case _:
				print("Invalid Choice! Choose 1 for withdrawal, 2 for balance enquiry and 3 to quit.")
	else:
		attempts += 1
		if attempts < max_attempts:
			print("Incorrect Pin! Try again!")
		else:
			print("Incorrect Pin! Your card has been blocked due to multiple failed attempts")
			exit()

	proceed = input("Would you like to perform another transaction? (1. Yes / 2. No): ")
	if proceed == "2":
		break

print("Thank you for using our services. Have a good day!")

