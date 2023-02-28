
import csv

# Define a function to validate the email address format
def is_valid_email(email):
    if len(email) > 7:
        if "@" in email and "." in email:
            return True
    return False

# Define a function to validate the date format
def is_valid_date(date):
    try:
        day, month, year = date.split("/")
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

# Prompt the user for flight information
while True:
    name = input("Enter name: ")
    email = input("Enter email: ")
    if not is_valid_email(email):
        print("Please enter a valid email address.")
        continue
    people = input("Enter the number of people: ")
    if not people.isnumeric() or int(people) < 1:
        print("Please enter a positive integer for the number of people.")
        continue
    destination = input("Enter destination: ")
    date = input("Enter date (DD/MM/YYYY): ")
    if not is_valid_date(date):
        print("Please enter a valid date in the format DD/MM/YYYY.")
        continue
    break

# Calculate the cost of the flight booking
cost = int(people) * 1.5 * 2 * 34.5 * 2

# Write the flight information to a CSV file
with open("flight.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, email, destination, date, people, cost])

print("Flight information added to file.")
