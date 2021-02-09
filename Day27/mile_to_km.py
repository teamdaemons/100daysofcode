from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter Project")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

input = Entry(width=10)
input.pack()
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.pack()
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.pack()
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0", font=("Arial", 24, "bold"))
km_result.pack()
km_result.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.pack()
km_label.grid(column=2, row=1)


def button_clicked():
    km = round(float(input.get()) * 1.609)
    km_result.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.pack()
button.grid(column=1, row=2)

window.mainloop()
