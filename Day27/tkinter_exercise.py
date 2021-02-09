from tkinter import *

window = Tk()
window.title("My first tkinter App")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.grid(column=0,row=0)



def button_clicked():
    my_label["text"] = "Button got Clicked"
    my_label.config(text=input.get())
    print("Button got Clicked")
    print(input.get())

# Button
button = Button(text="Click Me", command =button_clicked)
button.pack()
button.grid(column=1,row=1)

button = Button(text="Click Me2", command =button_clicked)
button.pack()
button.grid(column=2,row=0)

#Entry

input = Entry(width=10)
input.pack()
input.grid(column=3,row=2)
print(input.get())

window.mainloop()
