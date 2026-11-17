# Prepaid College Canteen Card System

card_balance = 500
correct_pin = 4321
attempt = 0
login = False

# PIN verification
while attempt < 3:
    entered_pin = int(input("Enter your card PIN: "))

    if entered_pin == correct_pin:
        print("Login Successful!")
        login = True
        break
    else:
        attempt += 1
        print("Wrong PIN!")

        if attempt < 3:
            print("Attempts left:", 3 - attempt)
        else:
            print("Your card is blocked.")

# Open menu after successful login
if login:
    while True:
        print("COLLEGE CANTEEN CARD ")
        print("1. Check Balance")
        print("2. Recharge Card")
        print("3. Make Purchase")
        print("4. Exit")
        print("5. View Transaction History")

        choice = input("Enter your choice: ")

#Check Balance

        if choice == "1":
            print("Available Balance: Rs.", card_balance)

#Recharge amount
        elif choice == "2":
            amount = float(input("Enter recharge amount: "))

            if amount <= 0:
                print("Enter a valid positive amount.")
                continue
            else:
                card_balance += amount
                print("Recharge successful!")
                print("Updated Balance:", card_balance)

#Purchase amount
        elif choice == "3":
            amount = float(input("Enter purchase amount: "))

            if amount <= 0:
                print("Invalid purchase amount.")
                continue
            elif amount > card_balance:
                print("Insufficient balance!")
            else:
                card_balance -= amount
                print("Purchase successful!")
                print("Remaining Balance:", card_balance)
                
#Exit Card
        elif choice == "4":
            print("Thank you for using the canteen card.")
            print("Final Balance:", card_balance)
            break

        elif choice == "5":
            # Transaction history feature will be added later
            pass

        else:
            print("Invalid choice. Please try again.")

