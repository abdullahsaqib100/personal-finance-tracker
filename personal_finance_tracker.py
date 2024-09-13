import csv

file_name = "expenses.csv"

def initialize_file():
    with open (file_name, mode = 'a+' , newline = '') as file:
        writer = csv.writer(file)
        file.seek(0)

        if file.read(1):
            return
        
        writer.writerow(["Date" , "Category" , "Description" , "Amount"])

# function to add expenses in the csv file
    
def add_expense(date, category, description, amount):
    with open(file_name, mode = 'a' , newline= '') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

        print("Expense Added Successfully!")

# function to show all the expenses from the csv file

def show_expenses():
    with open (file_name, mode= 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(', '.join(row))

# function to calculate total expenses

def total_expenses():
    total = 0
    with open (file_name , mode= "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[3])

    print(f" Total Expense is {total}")


# main function to run the program

def main():
    initialize_file()

    while True:

        print("\nOptions: ")
        print("1. Add a new expense: ")
        print("2. Show all expenses: ")
        print("3. Calculate the total expense: ")
        print("4. Exit")

        choise = input("Enter your choise: ")

        if choise == "1" :
            date = input("Enter the date (DD-MM-YYYY): ")

            category = input("Enter the category (e.g: Food, Bills, Transport): ")

            description = input("Enter the description: ")

            amount = input("Enter the amount: ")

            add_expense(date, category, description, amount) # calling the fuction "add_expense" to store the user entered data, into the csv file(expenses.csv)


        elif choise == "2":
            show_expenses()

        elif choise == "3":
            total_expenses()

        elif choise == "4" :
            print("Goodbye!")
            break

        else:
            print("You choosed invalid choise. Please Try Again")


if __name__ == "__main__":
    main()


    

        
        