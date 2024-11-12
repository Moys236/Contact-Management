contacts = {}
while True:
    print("""
Contact Management

1_ Add a contact
2_ View contact
3_ Edit a contact
4_ Exit
""")
    choice = int(input("Please choose a number from 1-4 "))
    if choice == 1:
        contacts["ID"] = input("Enter the contact ID: ")
        contacts["name"] = input("Please type a name: ")
        contacts["phone"] = int(input("Please type a phone number: "))
        print(f"\n\n{contacts['name']} was added successfully..")
    elif choice == 2 :
        print(contacts)
    elif choice == 3 :
        contacts["ID"] = input("Please enter an ID edit: ")
        contacts["name"] = input("Enter a new name: ")
        contacts["phone"] = int(input("enter a new number: "))
        print("Success ...")
    elif choice == 4:
        print("\n Exiting the program ....\n")
        break
    else :
        print("invalide choice.")
