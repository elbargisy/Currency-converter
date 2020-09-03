
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

def convert():
    result = round(float(entrybox.get()) * rate[currency_2.get()]/rate[currency_1.get()],2)
    convertedlbl.config(text=result)
    lbl2 = Label(window,text = 'this data is as on today : '+response['date'] ,font=('Times New Roman', 24, 'italic'),fg ='blue',bg ='CYAN')
    lbl2.place(x=100,y=200)

window = Tk()
window.title('currency converter')
window.geometry ('600x450')
window.config(bg='skyblue')
lbl1 = Label(window,text = ' Welcome to Currency Exchanger ',font=('Times New Roman', 24, 'italic'),fg ='blue',bg ='CYAN')
lbl1.place(x=120,y=20)

url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url).json()
rate =response['rates']

var_1 = StringVar(window)
var_1.set('Choose Currency')
var_2=StringVar(window)
var_2.set('Choose to Currency')

currency_1 = ttk.Combobox(window,value=list(rate.keys()),width=20,justify =CENTER,
                        font =('Times New Roman', 18, 'italic'),state = 'readonly')
currency_1.place(x= 20,y =80)

currency_2 = ttk.Combobox(window,text = var_2,value=list(rate.keys()),width=20,justify =CENTER,
                        font =("Times New Roman", 18, "italic"),state = 'readonly')
currency_2.place(x= 300,y =80)

entrybox = Entry(window, relief = tk.RIDGE, justify = tk.CENTER,font=('Times New Roman', 24, 'italic'))
entrybox.place(x= 20,y=300)

convertedlbl = Label(window,font=('Times New Roman', 24, 'italic'),fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
convertedlbl.place(x=300,y=300)

convertButn = Button(window,text ='Convert',justify ='center',font=('Times New Roman', 24, 'italic'),
        activebackground ='lightgreen',command =convert)
convertButn.place(x=230,y =380)

window.mainloop()
