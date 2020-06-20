import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from time import strftime
from financeValueCalc import currentValue, getTotalBalances 
from financePlot import plotBalance

# creating tkinter window 
root = Tk() 
root.title('Bean Counter') 

# Creating Menubar 
menubar = Menu(root)
f = open('userData.txt','w+')

def saveUserValues():
    f = open('userData.txt','w+')
    for key, value in financeInputs.items() :
        stingTowrite = key + ':' + str(value) + '\n'
        f.write(stingTowrite)
    f.close()

def getUserValuesfile():
    testDict = dict()
    with open('userData.txt') as f:
        for line in f:
            line = line.split(':')
            print(line)
            
# Adding File Menu and commands 
fileMenu = Menu(menubar, tearoff = 0)

subMenuSave = Menu(fileMenu)
subMenuOpen = Menu(fileMenu)

subMenuSave.add_command(label = "Save Values",command = saveUserValues)
subMenuOpen.add_command(label = "Get Previous Values", command = getUserValuesfile)

menubar.add_cascade(label ='File', menu = fileMenu)

fileMenu.add_command(label ='New File', command = None) 
fileMenu.add_cascade(label ='Open', menu = subMenuOpen) 
fileMenu.add_cascade(label ='Save', menu = subMenuSave) 
fileMenu.add_separator() 
fileMenu.add_command(label ='Exit', command = root.destroy) 

# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 

# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 



financeInputs = {'Initial Principal': 10000,
                 'Salary': 65000,
                 'Interest Annualy' : 0.07,
                 'Number Periods' : 12,
                 'Years Invested' : 30,
                 'Monthly Contribution' : 500.50,
                 'Company Match' : 0.04,
                 'Monthly Percent Contribution': 0.18
                 }

fields = ['Salary','Initial Principal','Interest Annualy', 'Number Periods','Monthly Contribution','Years Invested','Company Match','Monthly Percent Contribution']
defaultFields = ['65000', '10000','7.0','12','500.50','30','4.0','18.0']

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        financeInputs[field] = text
        print('%s: "%s"' % (field, text)) 
    
totalValue = StringVar()
inputStingText = StringVar()
def makeform(root, fields):
    entries = []
    i = 0
    for field in fields:
        lab = tk.Label(root, width=15, text=field, anchor='w')
        ent = tk.Entry(root)
        Label(root,text = field).grid(row=i+1,column = 0)
        ent.grid(row=1+i, column=1)
        ent.insert(0,defaultFields[i])
        entries.append((field, ent))
        i = i + 1
        
    totalValue.set("Please enter your values")
    Label(root,textvariable = totalValue).grid(row=i+1,column = 0,columnspan = 2)
    inputStingText.set(" ")
    Label(root,textvariable = inputStingText).grid(row=i+2,column = 0,columnspan=2)
   
    return entries

def getplot():
    totalBalances =getTotalBalances(float(financeInputs["Initial Principal"]),
                    float(financeInputs["Interest Annualy"])/100,
                    float(financeInputs["Number Periods"]),
                    float(financeInputs["Years Invested"]),
                    float(financeInputs["Monthly Contribution"]),
                    float(financeInputs["Salary"]),
                    float(financeInputs['Company Match'])/100,
                    float(financeInputs['Monthly Percent Contribution'])/100             
                     )
    
    fig, ax = plt.subplots()
    plotBalance(totalBalances,
            financeInputs["Years Invested"],
            financeInputs["Interest Annualy"],
            ax
            )

    finalValue = int(totalBalances[-1])
    intputText = 'Using initial pricipal of ' + str(financeInputs["Initial Principal"]) + ', ' + 'number years ' + str(financeInputs["Years Invested"])
    totalText = 'Your total value is: ' + '{:,}'.format(finalValue) + '$'
    totalValue.set(totalText)
    inputStingText.set(intputText)
    
    plt.show()

btn_plot= tk.Button(root, text="Plot", command=getplot)
btn_plot.grid(row=0, column=0)
root.geometry("500x500")
root.config(menu = menubar)


ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e)))

mainloop() 
