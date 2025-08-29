import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Finance App Setup Test")

# Chart Example
fig, ax = plt.subplots()
ax.plot([100, 200, 150, 300, 250], marker='o')
ax.set_title("Test Chart - Monthly Expenses")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
