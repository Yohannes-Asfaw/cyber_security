def cipher(str1):
    jump = int(input("insert the jump for the cipher encryption: "))
    if jump > 26:
        jump = jump % 26
    str2 = ""
    for i in str1:
        if i == " ":
            str2 += " "
        elif ord(i) + jump > 122:
            tempo = ord(i) + jump - 26
            str2 += chr(tempo)
        else:
            str2 += chr(ord(i) + jump)
    return str2
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')


# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=5,
                   width=20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
                        text="Print",
                        command=printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
