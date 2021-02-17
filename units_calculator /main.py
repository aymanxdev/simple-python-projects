from tkinter import *

window = Tk()
window.title("Mile to KM")
window.config(padx=50, pady=50)

label_title = Label(text="Convertor")
label_title.grid(column= 1, row=0)


my_label = Label(text="Miles")
my_label.grid(column= 2, row= 1)

second_label = Label(text='is equal to')
second_label.grid(column= 0, row= 1)

third_label = Label(text='Km')
third_label.grid(column= 2, row= 2)

result_label = Label(text="0")
result_label.grid(column= 1, row= 2)

def onClick():
    mile_input = input.get()
    result = round(int(mile_input) * 1.609)
    result_label.config(text=result)


button = Button(text="Calculate", command=onClick)
button.grid(column=1,row= 3)


#entry
input = Entry(width=10)
input.grid(column=1, row=1)


#Listbox
#more calculation formulas can be added here
def listbox_clicked(event):
    option = listbox.get(listbox.curselection())
    if option == "KM":
        mile_input = input.get()
        result = round(int(mile_input) * 1.609)
        result_label.config(text=result)
    elif option == "Meters":
        mile_input = input.get()
        result = round(int(mile_input) * 1609, 2)
        result_label.config(text=result)

listbox  = Listbox(height=4)
#more units can be added to the list below
options = ["KM", "Meters"]
for item in options:
    listbox.insert(options.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_clicked)
listbox.grid(column = 1, row =4)


window.mainloop()