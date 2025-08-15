print("Welcome to the ATM")
print("Kindly insert your card")
balance = (10000)
pin = int(input("Enter pin:"))
if pin == 1234:
    print(balance)
    print("pin is correct, Enter the following options")
    Balance_inquiry = int(input('Press 1 for Balance Inquiry:'))
    if Balance_inquiry == 1:
        print("Your balance is:", balance)
