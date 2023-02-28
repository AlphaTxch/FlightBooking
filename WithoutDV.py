"""import csv

name = input("Enter name: ")
email = input("Enter email: ")
people=int(input("Enter the amount of people:"))
destination = input("Enter destination: ")
date = input("Enter date: ")
#cost = input("Enter cost: ")
cost=people*1.5*2*34.5*2
print("This is how much it will cost: GBP",cost)
with open("flight.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, email, destination, date, people,cost])

print("Flight information added to file.")
"""
"""
import csv

name = input("Enter name: ")
email = input("Enter email: ")
people = int(input("Enter the amount of people: "))
destination = input("Enter destination: ")
date = input("Enter date: ")
#cost = input("Enter cost: ")
cost = people * 1.5 * 2 * 34.5 * 2
print("This is how much it will cost: GBP", cost)

# Write flight information to CSV file
with open("flight.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, email, destination, date, people, cost])
print("Flight information added to file.")

# Read flight information from CSV file
with open("flight.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        """


import csv
import requests

# Constants
GBP_TO_USD_RATE = 1.38
SEAT_ROWS = 20
SEAT_COLS = 6

# Get currency conversion rate
response = requests.get("https://api.exchangeratesapi.io/latest?base=GBP")
if response.status_code == 200:
    try:
        data = response.json()
        GBP_TO_EUR_RATE = data["rates"]["EUR"]
    except (KeyError, TypeError):
        # If the response doesn't contain a "rates" field or is not JSON, use a default rate
        GBP_TO_EUR_RATE = 1.16
else:
    # If the request fails, use a default rate
    GBP_TO_EUR_RATE = 1.16

# Get user inputs
name = input("Enter name: ")
email = input("Enter email: ")
people = int(input("Enter the amount of people: "))
destination = input("Enter destination: ")
date = input("Enter date (YYYY-MM-DD): ")

# Calculate cost in GBP and EUR
cost_gbp = people * 1.5 * 2 * 34.5 * 2
cost_eur = cost_gbp * GBP_TO_EUR_RATE

# Convert cost to USD
cost_usd = cost_gbp * GBP_TO_USD_RATE

# Display cost in all currencies
print(f"This is how much it will cost: GBP {cost_gbp:.2f}, EUR {cost_eur:.2f}, USD {cost_usd:.2f}")

# Get seat selection from user
print("Please select your seat:")
seats = [["" for col in range(SEAT_COLS)] for row in range(SEAT_ROWS)]
for row in range(SEAT_ROWS):
    for col in range(SEAT_COLS):
        seat_label = f"{chr(row + ord('A'))}{col + 1:02d}"
        if seats[row][col] == "":
            print(f"{seat_label} [ ]", end=" ")
        else:
            print(f"{seat_label} [X]", end=" ")
    print()
seat_selection = input("Enter seat selection (e.g. A01 B02 C03): ")
for seat_label in seat_selection.split():
    row = ord(seat_label[0]) - ord('A')
    col = int(seat_label[1:]) - 1
    seats[row][col] = "X"
print("Seat selection:")
for row in range(SEAT_ROWS):
    for col in range(SEAT_COLS):
        print(seats[row][col], end=" ")
    print()

# Add flight information to CSV file
with open("flight.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, email, destination, date, people, cost_gbp])
print("Flight information added to file.")

# Display flight status
print("Flight status: on time")

# Print receipt
print()
print("=" * 40)
print("RECEIPT")
print("=" * 40)
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Date: {date}")
print(f"Destination: {destination}")
print(f"Number of people: {people}")
print(f"Cost: GBP {cost_gbp:.2f}")
print("=" * 40)
