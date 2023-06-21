from tkinter import *

def miles_to_kilometers():
    miles = float(miles_input.get())
    km = round(1.609 * miles)
    km_result_label.config(text=f'{km}')


window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=50, pady=50)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

km_result_label = Label(text='0')
km_result_label.grid(column=1, row=1)

calculate_button = Button(text='Calculate', command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)


window.mainloop()