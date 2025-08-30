import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import expense_entry

#test data
expenses = {
    "Food": 3870,
    "Rent": 6750,
    "Cigs": 3500,
    "Travel": 700,
    "Misc": 2030,
    "Utilities": 2100
}

root = tk.Tk()
root.title("Finance App Setup Test")

'''# Chart Example
fig, ax = plt.subplots()
ax.plot([100, 200, 150, 300, 2520], marker='o')
ax.set_title("Test Chart - Monthly Expenses")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
'''


expense_entry.pie_chart(root, expenses)

root.mainloop()


