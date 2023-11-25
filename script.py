import tkinter as tk

def jj(num):
    if num == '←':
        text.delete(len(text.get())-1)
    else:
        if num == "X":
            n = "*"
            text.insert(tk.END, n)
        elif num == "÷":
            n = "/"
            text.insert(tk.END, n)
        else:
            text.insert(tk.END, num)

def cc():
    text.delete(0, tk.END)
    label.config(text="")

def math():
    try:
        get = eval(text.get())
    except:
        label.config(text="완성되지 않은 수식입니다.")
    else:
        label.config(text=get)

    
    

root = tk.Tk()

root.title('계산기')
root.resizable(False, False)
root.config(padx=10, pady=10, bg='#81F7F3')

button = [
    ['7', '8', '9', 'X'],
    ['4', '5', '6', '÷'],
    ['1', '2', '3', '-'],
    ['0', '.', '←', '+']
]

text = tk.Entry(root, width=30, font=("Open Sans", 20), justify='right')
text.grid(column=0, row=0, columnspan=4)
text.focus()

label = tk.Label(root, text="", width=20, font=('Open Sans', 30), bg='#81F7F3')
label.grid(row=1, column=0, columnspan=4, pady=15)

for i in range(4):
    for j in range(4):
        a = button[i][j]
        button2 = tk.Button(root, text=a, width=8, font=('Open Sans', 15), bg='#FBFBEF', command=lambda wow=a: jj(wow))
        button2.grid(row=i+2, column=j, pady=1.5)

c = tk.Button(root, text="c", width=17, font=('Open Sans', 15), bg='#FBFBEF', command=cc)
c.grid(column=0, row=6, columnspan=2, pady=5)

b = tk.Button(root, text="=", width=17, font=('Open Sans', 15), bg='#FBFBEF', command=math)
b.grid(column=2, row=6, columnspan=2, pady=5)

root.mainloop()