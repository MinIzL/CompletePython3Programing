import tkinter as tk
import math

def BMICriteria(testNum):
    if testNum >= 30:
        labelconsidered.configure(text='อ้วนมาก')
    elif testNum >= 25.0 < 29.9:
        labelconsidered.configure(text='อ้วน')
    elif testNum >= 23.0 <= 24.9:
        labelconsidered.configure(text='น้ำหนักเกิน')
    elif testNum >= 18.6 <= 22.0:
        labelconsidered.configure(text='น้ำหนักปกติ เหมาะสม')
    else:
        labelconsidered.configure(text='ผอมเกินไป')

def leftClick(event):
    testNum = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100, 2)
    labelResult.configure(text='%.1f' %(testNum))
    BMICriteria(testNum)

MainWindow = tk.Tk()
labelHeight = tk.Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = tk.Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = tk.Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = tk.Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = tk.Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClick)
calculateButton.grid(row=2,column=0)
labelResult = tk.Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelconsidered = tk.Label(MainWindow,text="ผลประเมิน")
labelconsidered.grid(row=2,column=2)

MainWindow.mainloop()