import tkinter as tk # Importing tkinter for GUI
from tkinter import ttk # Importing ttk for themed widgets
from tkinter import messagebox # Importing messagebox for dialog boxes
import matplotlib.pyplot as plt # Importing matplotlib for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Embedding matplotlib in tkinter

# Main application class 
# Chart Example
fig, ax = plt.subplots()
ax.plot([100, 200, 150, 300, 2520], marker='o')
ax.set_title("Test Chart - Monthly Expenses")

class FinanceApp: # Class for the finance application
    def __init__(self, root): # Initializing the application
        self.root = root # Root window
        self.root.title("Personal Finance Manager") # Setting window title
        self.root.geometry("800x600") # Setting window size


        # Initialize data structures
        self.income = [] # List to store income entries
# Main application class 

class FinanceApp: # Class for the finance application
    def __init__(self, root): # Initializing the application
        self.root = root # Root window
        self.root.title("Personal Finance Manager") # Setting window title
        self.root.geometry("800x600") # Setting window size
        self.create_widgets() # Call method to create UI components
        
    # UI Components
    
    def create_widgets(self): # Method to create UI components
        # Frame for input fields
        input_frame = ttk.Frame(self.root) # Frame for input fields
        input_frame.pack(pady=10) # Packing the frame with padding
        # Initialize data structures
        self.income = [] # List to store income entries
        self.expenses = [] # List to store expense entries

        # Create UI components
        self.create_widgets() # Call method to create UI components
        
    # UI Components
    
    def create_widgets(self): # Method to create UI components
        # Frame for input fields
        input_frame = ttk.Frame(self.root) # Frame for input fields
        input_frame.pack(pady=10) # Packing the frame with padding

        # Income input
        ttk.Label(input_frame, text="Income:").grid(row=0, column=0, padx=5, pady=5) # Label for income
        self.income_entry = ttk.Entry(input_frame) # Entry for income
        self.income_entry.grid(row=0, column=1, padx=5, pady=5) # Placing the entry in the grid
        ttk.Button(input_frame, text="Add Income", command=self.add_income).grid(row=0, column=2, padx=5, pady=5) # Button to add income

        # Expense input
        ttk.Label(input_frame, text="Expense:").grid(row=1, column=0, padx=5, pady=5) # Label for expense
        self.expense_entry = ttk.Entry(input_frame) # Entry for expense
        self.expense_entry.grid(row=1, column=1, padx=5, pady=5) # Placing the entry in the grid
        ttk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=1, column=2, padx=5, pady=5) # Button to add expense

        # Frame for buttons
        button_frame = ttk.Frame(self.root) # Frame for buttons
        button_frame.pack(pady=10) # Packing the frame with padding

        # Buttons for actions
        ttk.Button(button_frame, text="Show Summary", command=self.show_summary).grid(row=0, column=0, padx=5, pady=5) # Button to show summary
        ttk.Button(button_frame, text="Show Chart", command=self.show_chart).grid(row=0, column=1, padx=5, pady=5) # Button to show chart

        # Text area for summary
        self.summary_text = tk.Text(self.root, height=10) # Text area for summary
        self.summary_text.pack(pady=10) # Packing the text area with padding
        self.summary_text.config(state=tk.DISABLED) # Making the text area read-only

    # Button Actions
    def add_income(self): # Method to add income
        try:   # Try block to catch errors
            amount = float(self.income_entry.get())    # Get the amount from entry and convert to float
            self.income.append(amount)  # Append the amount to income list
            self.income_entry.delete(0, tk.END)     # Clear the entry field
            messagebox.showinfo("Success", "Income added successfully!")        # Show success message
        except ValueError:                  # Catch ValueError if conversion fails
            messagebox.showerror("Error", "Please enter a valid number.")           # Show error message

    def add_expense(self): # Method to add expense
        try:
            amount = float(self.expense_entry.get())
            self.expenses.append(amount)
            self.expense_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def show_summary(self):
        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete(1.0, tk.END)
        total_income = sum(self.income)
        total_expenses = sum(self.expenses)
        balance = total_income - total_expenses
        self.summary_text.insert(tk.END, f"Total Income: {total_income}\n")
        self.summary_text.insert(tk.END, f"Total Expenses: {total_expenses}\n")
        self.summary_text.insert(tk.END, f"Balance: {balance}\n")
        self.summary_text.config(state=tk.DISABLED)

    def show_chart(self):   # Method to show chart
        # Example static chart
        categories = ["Food", "Rent", "Transport", "Entertainment"]     # Example categories
        amounts = [300, 800, 150, 200] # Example amounts

        # Create a frame for the chart if it doesn't exist
        if not hasattr(self, 'chart_frame'):
            self.chart_frame = ttk.Frame(self.root)
            self.chart_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Clear previous chart if any
        for widget in self.chart_frame.winfo_children():    # Clear previous chart if any
            widget.destroy() # Destroy previous widgets

        fig, ax = plt.subplots(figsize=(5, 4)) # Create a new figure
        ax.pie(amounts, labels=categories, autopct="%1.1f%%") # Create pie chart
        ax.set_title("Expenses by Category") # Set chart title

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame) # Embed the chart in tkinter
        canvas.draw() # Draw the canvas
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Pack the canvas

if __name__ == "__main__":  # Main block to run the application
    root = tk.Tk() # Create root window
    app = FinanceApp(root) # Create instance of FinanceApp
    root.mainloop() # Start the main event loop
