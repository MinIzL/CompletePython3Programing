import tkinter as tk
import math

def leftClick(event):
    labelResult.configure(text='%.2f' %(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)))

MainWindow = tk.Tk()
labelHeight = tk.Label(MainWindow, text="Height (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = tk.Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = tk.Label(MainWindow, text="Weight (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = tk.Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = tk.Button(MainWindow,text = "Calculate")
calculateButton.bind('<Button-1>', leftClick)
calculateButton.grid(row=2,column=0)
labelResult = tk.Label(MainWindow,text="Result")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()