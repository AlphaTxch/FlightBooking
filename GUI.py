import tkinter as tk
import tkinter.messagebox as messagebox
import csv

class FlightBookingApp:
    def __init__(self, master):
        self.master = master
        master.title("Flight Booking App")

        # Create input fields
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)

        self.email_label = tk.Label(master, text="Email:")
        self.email_entry = tk.Entry(master)

        self.people_label = tk.Label(master, text="Number of People:")
        self.people_entry = tk.Entry(master)

        self.destination_label = tk.Label(master, text="Destination:")
        self.destination_entry = tk.Entry(master)

        self.date_label = tk.Label(master, text="Date:")
        self.date_entry = tk.Entry(master)

        # Create buttons
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.cancel_button = tk.Button(master, text="Cancel", command=master.quit)

        # Layout widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        self.email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1)

        self.people_label.grid(row=2, column=0)
        self.people_entry.grid(row=2, column=1)

        self.destination_label.grid(row=3, column=0)
        self.destination_entry.grid(row=3, column=1)

        self.date_label.grid(row=4, column=0)
        self.date_entry.grid(row=4, column=1)

        self.submit_button.grid(row=5, column=0)
        self.cancel_button.grid(row=5, column=1)

    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        people = int(self.people_entry.get())
        destination = self.destination_entry.get()
        date = self.date_entry.get()

        # Calculate cost
        cost = people * 1.5 * 2 * 34.5 * 2

        # Write to CSV file
        with open("flight.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, destination, date, people, cost])

        # Show confirmation message
        messagebox.showinfo("Booking Confirmed", "Your flight has been booked.")

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.people_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

root = tk.Tk()
app = FlightBookingApp(root)
root.mainloop()
