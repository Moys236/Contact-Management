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
        contact_ID = input("Enter the contact ID: ")
        contact_name = input("Please type a name: ")
        contact_phone = input("Please type a phone number: ")
        while True :
                if contact_phone.isdigit():
                    break
                else :
                    contact_phone = input("Please enter a number as digits: ")
        contacts[contact_ID] = {"name":contact_name, "phone":contact_phone}
        print(f"\n\n{contact_name} was added successfully..")
    elif choice == 2 :
        print(contacts)
    elif choice == 3 :
        id_to_edit = input("Please enter an ID edit: ")
        if id_to_edit in contacts:
            new_name = input("Enter a new name: ")
            new_phone = input("enter a new number: ")
            while True :
                if new_phone.isdigit():
                    break
                else :
                    new_phone = input("Please enter a number as digits: ")
            contacts[id_to_edit] = {"name":new_name ,"phone":new_phone}
            print("Success ...")
        else:
            print(f"Sorry, {id_to_edit} was not found ....")
    elif choice == 4:
        print("\n Exiting the program ....\n")
        break
    else :
        print("invalide choice.")
