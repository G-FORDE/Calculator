# calculator by Gregory Forde
# gregoryforde1984@gmail.com
# Github.com/g-forde/

from tkinter import *

# click event
def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


# clear button
def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")


# equals button
def btn_equals_input():
    global operator
    total = str(eval(operator))
    text_Input.set(total)
    operator = ""


cal = Tk()
cal.title("GF Calculator")
operator = ""
text_Input = StringVar()

#text properties, gui design
txtDisplay = Entry(cal, font=("arial", 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify="right").grid(columnspan=4)

# buttons
# row1===========================================================================================================================

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="7", bg="powder blue", command=lambda: btn_click(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="8", bg="powder blue", command=lambda: btn_click(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="9", bg="powder blue", command=lambda: btn_click(9)).grid(row=1, column=2)

Addition = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                  text="+", bg="powder blue", command=lambda: btn_click("+")).grid(row=1, column=3)

# row2===========================================================================================================================

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="4", bg="powder blue", command=lambda: btn_click(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="5", bg="powder blue", command=lambda: btn_click(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="6", bg="powder blue", command=lambda: btn_click(6)).grid(row=2, column=2)

Subtraction = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                     text="-", bg="powder blue", command=lambda: btn_click("-")).grid(row=2, column=3)

# row3===========================================================================================================================


btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="1", bg="powder blue", command=lambda: btn_click(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="2", bg="powder blue", command=lambda: btn_click(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="3", bg="powder blue", command=lambda: btn_click(3)).grid(row=3, column=2)

Multiply = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                  text="*", bg="powder blue", command=lambda: btn_click("*")).grid(row=3, column=3)

# row4===========================================================================================================================

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
              text="0", bg="powder blue", command=lambda: btn_click(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                  text="C", bg="powder blue", command=btn_clear_display).grid(row=4, column=1)

btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                   text="=", bg="powder blue", command=btn_equals_input).grid(row=4, column=2)

Division = Button(cal, padx=16, pady=16, bd=8, fg="black", font=("ariel", 20, "bold"),
                  text="/", bg="powder blue", command=lambda: btn_click("/")).grid(row=4, column=3)

cal.mainloop()
