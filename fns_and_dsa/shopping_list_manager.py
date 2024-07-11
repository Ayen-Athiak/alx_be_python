shopping_list =[]
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def add_item():
    item =input("Enter the item to add:")
    shopping_list.append(item)
    print(item)

def remove_item():
    item= input("Enter the item to remove:")
    if  item in shopping_list:
        shopping_list.remove(item)
        print("the item has been remove")
    else:print("the item you enter is not in the shopping list")
def view_item():
    print(shopping_list)
    if shopping_list:
        for items in shopping_list:
            print(items)
    else:print("your shopping list is empty")





def main():
    shopping_list = []
    while True:
        display_menu()
        choice =int(input("Enter the item to add: "))

        if choice == '1':
            add_item()
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item()
            # Prompt for and remove an item
            pass
        elif choice == '3':
            view_item()
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()