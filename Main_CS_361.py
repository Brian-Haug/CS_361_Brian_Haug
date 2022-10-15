# Brian Haug

import csv

# Adding list as value
Watches_1 = ["1", "Seiko", "SRPH77", "$55"]
Watches_2 = ["2", "Timex", "Expedition", "$35"]
Watches_3 = ["3", "Tissot", "PR 516", "$295"]
Watches_4 = ["4", "Omega", "Seamaster", "$2500"]
Watches_5 = ["5", "Rolex", "Submariner", "$5500"]
Watches_6 = ["6", "Casio", "Edifice", "$75"]
Watches_7 = ["7", "Seiko", "Solar", "$255"]
Watches_8 = ["8", "Seiko", "Kinetic", "$345"]
Watches_9 = ["9", "Casio", "Calculator", "$125"]
Watches_10 = ["10", "Tissot", "PRX", "$375"]

Watches = [Watches_1, Watches_2, Watches_3, Watches_4, Watches_5, Watches_6, Watches_7, Watches_8, Watches_9,
           Watches_10]


def print_current_inventory(inventory_list):
    Watches = inventory_list

    headings = ["ITEM NUMBER", "BRAND", "MODEL", "PRICE"]
    spacer = ["-----------", "-----", "-----", "-----"]

    for i in range(len(headings)):
        print(' {:15}      '.format(headings[i]), end='')

    print()

    for i in range(len(spacer)):
        print(' {:15}      '.format(spacer[i]), end='')

    print()

    for i in range(len(Watches)):
        for j in range(len(Watches[i])):
            print(' {:15}      '.format(Watches[i][j]), end='')
        print()

    print()


def home_page(inventory_list):
    print_current_inventory(inventory_list)

    print("Type the appropriate number to view the corresponding page:")
    print("1 - Edit")
    print("2 - Inventory")
    print("3 - Status")
    print("4 - New")

    home_page_input_1 = input()

    if home_page_input_1 == ("1"):
        edit_page(Watches)

    elif home_page_input_1 == ("2"):
        inventory_page(Watches)

    elif home_page_input_1 == ("4"):
        new_item_page(Watches)


def inventory_page(inventory_list):

    print("The inventory list will be downloaded as a CSV file.")

    with open('Watch_Data.csv', mode='w') as watches_file:
        file_writer = csv.writer(watches_file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(inventory_list)

    print("Download complete.")

def new_item_page(inventory_list):
    new_input_1 = input("Enter the Brand name: ")
    new_input_2 = input("Enter the Model name: ")
    new_input_3 = input("Enter the Price: ")

    inventory_list.append([str(len(inventory_list) + 1),new_input_1, new_input_2, new_input_3])


def edit_page(inventory_list):
    while True:

        edit_input_1 = int(input("Enter the item number you want to edit:"))

        print("The following item will be edited: ", end=" ")

        print(inventory_list[edit_input_1 - 1])

        print("Type the appropriate number to edit the corresponding section:")
        print("1 - Item Manufacturer")
        print("2 - Item Model")
        print("3 - Item Price")

        while True:

            edit_input_2 = input()

            if edit_input_2 == "1":
                print("The following will be edited: Item Manufacturer")
                edit_input_3 = input("Enter the text you want to replace for the Item Manufacturer:")
                inventory_list[edit_input_1 - 1][1] = edit_input_3
                break

            elif edit_input_2 == "2":
                print("The following will be edited: Item Model")
                edit_input_3 = input("Enter the text you want to replace for the Item Model:")
                inventory_list[edit_input_1 - 1][2] = edit_input_3
                break

            elif edit_input_2 == "3":
                print("The following will be edited: Item Price")
                edit_input_3 = input("Enter the text you want to replace for the Item Price:")
                inventory_list[edit_input_1 - 1][3] = edit_input_3
                break

            elif edit_input_2 == "Home":
                home_page(inventory_list)
                break

            else:
                print("Invalid entry, try again: ")
                continue

        if edit_input_2 == "Home":
            break

        edit_input_4 = input("Do you want to edit another item? Enter Yes or No: ")

        if edit_input_4 == "Yes":
            continue
        else:
            break

while True:
    home_page(Watches)

    main_loop_input = input("Do you want to return to the Homepage or Quit? (Home/Quit): ")

    if main_loop_input == "Home":
        continue
    elif main_loop_input =="Quit":
        break
    else:
        print("Invalid input,try again: ")
        continue

