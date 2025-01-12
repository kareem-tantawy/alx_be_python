def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            shopping_list.append(input("Enter the new item: "))

        elif choice == "2":
            shopping_list.remove(input("Enter the item you want to remove: "))

        elif choice == "3":
            print("Displaying all items in your shopping list ....")
            for i in shopping_list:
                print(i)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
