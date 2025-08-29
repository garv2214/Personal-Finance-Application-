import tkinter as tk # Importing tkinter for GUI
from tkinter import ttk # Importing ttk for themed widgets
from tkinter import messagebox # Importing messagebox for dialog boxes
import matplotlib.pyplot as plt # Importing matplotlib for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Embedding matplotlib in tkinter

# Main application class 

class FinanceApp: # Class for the finance application
    def __init__(self, root): # Initializing the application
        self.root = root # Root window
        self.root.title("Personal Finance Manager") # Setting window title
        self.root.geometry("800x600") # Setting window size

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
        
        #Button Actions
    def add_income(self): # Method to add income
        try:   # Try block to catch errors
            amount = float(self.income_entry.get())    # Get the amount from entry and convert to float
            self.income.append(amount)  # Append the amount to income list
            self.income_entry.delete(0, tk.END)     # Clear the entry field
            messagebox.showinfo("Success", "Income added successfully!")        # Show success message
        except ValueError:                  # Catch ValueError if conversion fails
            messagebox.showerror("Error", "Please enter a valid number.")           # Show error message
    
    def add_transaction(self):  # Method to add transaction
        messagebox.showinfo("Add Transaction", "This feature will open a form to add transactions.")        # Show info message

    def view_transactions(self):    # Method to view transactions
        messagebox.showinfo("View Transactions", "This feature will display all transactions.")      # Show info message

    def show_chart(self):   # Method to show chart
        # Example static chart
        categories = ["Food", "Rent", "Transport", "Entertainment"]     # Example categories
        amounts = [300, 800, 150, 200] # Example amounts

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