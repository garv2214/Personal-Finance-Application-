import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#function to create a pie chart based on the expenses entered by the user with the labels for the expese. 
#the labels that can be used in the app should be provided to the user as options so that the input doest 
#become invalid.
#Parameters:
        #root: The Tkinter root or a frame to attach the chart to
        #expenses: Dictionary {category: amount}

# To Add Later: manual parsing for labels to make it user friendly
# To Add Later: color integrated user interface to make the pie chart more intuitive

def pie_chart(root, expenses):

    #create figure
    fig, ax = plt.subplots()

    category = list(expenses.keys())
    amounts = list(expenses.values())

    #plot the pie chart
    ax.pie(amounts, labels=category, autopct='%1.1f%%', startangle=90)
    ax.set_title("Monthly Expenses Breakdown")

    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()