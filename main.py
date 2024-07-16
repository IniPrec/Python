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
attempts = 0

while attempts < 3:
	pin = int(input("Enter your four-digit pin: "))
	if pin == user['pin']:
		while not quit:
			print("What do you want to do?\n")
			choice = int(input(print("1. Withdrawal\n2. Balance\n3. Quit\n")))
			if choice == 1:
				withdrawal()
			elif choice == 2:
				balance()
			elif choice == 3:
				quit = True
			else:
				print("Invalid choice!")
	else:
		print("Invalid Pin. Try again!")
		attempts += 1
		if attempts == 3:
			print("Your card has been blocked due to multiple failed attempts")