total_bill = 0
while True:
    print("Welcome to our restaurant \n=====Menu=====")
    print("1. Fried Chicken")
    print("2. Burger")
    print("3. Pizza")
    print("4. Sandwich")
    print("5. Exit")
    
    choice = input("Enter your choice:")

    if choice == "1":
        print("You choose Fried Chicken")
        price = 100
        print("Price: 100 Tk")
        quantity = int(input("Enter quantity: "))
        item_bill = price*quantity
        print("Price for Chicken fry= ", item_bill)
        total_bill+=item_bill

    elif choice == "2":
        print("You choose Burger")
        price = 120
        print("Price: 120 Tk")
        quantity = int(input("Enter quantity: "))
        item_bill = price*quantity
        print("Price for Burger= ", item_bill)
        total_bill+=item_bill


    elif choice == "3":
        print("You choose Pizza")
        price = 250
        print("Price: 250 Tk")
        quantity = int(input("Enter quantity: "))
        item_bill = price*quantity
        print("Price for Pizza= ", item_bill)
        total_bill+=item_bill



    elif choice == "4":
        print("You choose Sandwich")
        price = 80
        print("Price: 80 Tk")
        quantity = int(input("Enter quantity: "))
        item_bill = price*quantity
        print("Price for Sandwich= ", item_bill)
        total_bill+=item_bill

    
     
    elif choice == "5":
     print("Thanks for your order, Sir! \nYour total bill-", total_bill)
     break
    else:
        print("Invalid choice")
     
