import csv

def calculate_total_revenue():
    total_revenue = 0
    with open("flight.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            if len(row) < 6: # check if row has the expected number of columns
                continue
            cost = float(row[5])
            total_revenue += cost
    return total_revenue

total_revenue = calculate_total_revenue()
print("Total revenue from all flights: GBP", total_revenue)
