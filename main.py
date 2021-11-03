# Arsenij Vostrikov TA-20V
# Ma võin seda teha ilusam, regeksiga aga see võttab paar päeva rohkem aega


# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("task_info.txt", mode="r", encoding="utf-8")
    file1 = file.readlines()
    rows = []
    for row in file1:
        rows.append(list(map(strip, row.split(', '))))
    return rows

# this function writes contacts to file
def write_database(db):
    with open("task_info.txt", "w", encoding='utf-8') as file:
        data = []
        print(db)
        for row in db:
            data.append(", ".join(row) + "\n")
        print(db)
        file.write("".join(data))

def add_data_database(db):
    db = read_database()
    file = open("task_info.txt", mode="a", encoding="utf-8")
    string = input("enter data you want to add, using ', ' as delimiter\nadd folowing data as\nName\t\tPhone\t\t\tAge\tEmail\n")

    file.writelines("\n" + string)
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    db = read_database()
    print("Index \t Name \t\t Phone \t\t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")


def edit_data(db):
    print("Editing contact.")
    print_out_database(db)
    index = int(input("choose the position of user you need to change\n"))
    pos = db[index]
    print(pos)
    field = int(input("what data do you want do change\n1.name\n2.Phone\n3.Age\n4.Email\n"))-1
    print("old data:" + pos[field])
    newData = input("enter new data\n")
    pos[field] = newData
    print(db)
    write_database(db)

def converttostr(input_seq, seperator):
   final_str = seperator.join(input_seq)
   return final_str


def print_out_commands():
    db = read_database()
    while True:
        try:
            chose = int(input("\n\nThis is an data base program. What would you like to do? \n1.Enter Program\n2.Exit program\n"))
            if (chose == 1):
                while True:
                    try:
                        print("\n\nCommands are:")
                        print("1. list users")
                        print("2. edit user")
                        print("3. add user")
                        print("4. exit")
                        choose = int(input("\nWhat is your command?: \n"))
                        if (choose == 1):
                            print_out_database(db)
                        elif (choose == 2):
                            print("editing data")
                            edit_data(db)
                        elif (choose == 3):
                            print("adding data")
                            add_data_database(db)
                        elif (choose == 4):
                            break

                    except ValueError:
                        print("only ints are allowed")
            else:
                break
        except ValueError:
            print("only ints are allowed")

def main():
    db = read_database()
    print(db)
    print_out_commands()


main()