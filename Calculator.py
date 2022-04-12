from tkinter import *

IVORY = "#FFE4C0"
PINK = "#FFBBBB"
BLUE = "#BFFFF0"
GREEN = "#BFFFF0"

def clicked(digit):
    if digit == "<-":
        #하나씩 숫자 삭제
        input_entry.delete(len(input_entry.get())-1)
    else:
        input_entry.insert(END, digit)

def del_digit():
    input_entry.delete(0, END)
    result_label.config(text="")

def calculate():
    try:
        result = eval(input_entry.get())
    except:
        result_label.config(text="계산식 오류")
    else:
        result_label.config(text=result)


window = Tk()
window.title("계산기")
window.resizable(False, False)
window.config(padx=10, pady=10, bg=IVORY)

digits = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['0', '.', '<-', '+']
]

input_entry = Entry(window, width=30, font=("나눔바른펜", 20), 
bg = IVORY, justify=RIGHT)
input_entry.grid(column=0, row=0, columnspan=4)
input_entry.focus()

result_label = Label(window, text="", width=20, font=("나눔바른펜",30), bg=IVORY)
result_label.grid(column=0, row=1, columnspan=4)

for r in range(4):
    for c in range(4):
        digit = digits[r][c]
        button = Button(window, text=digit, width=8, font=("나눔바른펜",15), bg=PINK, command=lambda x=digit: clicked(x))
        button.grid(row=r+2, column=c, pady=2)

clear_button = Button(window, text="C", width=17, font=("나눔바른펜", 15, "bold"), bg=BLUE, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2, pady=5)

cal_button = Button(window, text="=", width=17, font=("나눔바른펜", 15, "bold"), bg=BLUE, command=calculate)
cal_button.grid(column=2, row=6, columnspan=2, pady=5)
window.mainloop()