import tkinter as tk

def calculate():
    try:
        expression = output.get('1.0', 'end-1c')  
        result = eval(expression)
        output.delete('1.0', 'end')  
        output.insert('1.0', str(result)) 
    except Exception as e:
        output.delete('1.0', 'end')
        output.insert('1.0', "Error")

def button_click(value):
    current_text = output.get('1.0', 'end-1c')  
    if current_text == "Error":
        output.delete('1.0', 'end')
    output.insert('end', value)  

def clear():
    output.delete('1.0', 'end')  


app = tk.Tk()
app.geometry('360x480')  
app.title('Calculator')


app.configure(bg='#F0F0F0')  


output = tk.Text(app, width=30, height=2, font=('Poppins', 20))
output.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


for i in range(1, 10):
    row_num = (i - 1) // 3 + 1
    col_num = (i - 1) % 3
    button = tk.Button(app, text=str(i), command=lambda value=str(i): button_click(value),
                       width=8, height=3, font=('Poppins', 20))
    button.grid(row=row_num, column=col_num, padx=5, pady=5)


button_0 = tk.Button(app, text='0', command=lambda value='0': button_click(value),
                      width=8, height=3, font=('Poppins', 20))
button_0.grid(row=4, column=1, padx=5, pady=5)


operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(app, text=operator, command=lambda value=operator: button_click(value),
                       width=8, height=3, font=('Poppins', 20))
    button.grid(row=i + 1, column=3, padx=5, pady=5)


equals_button = tk.Button(app, text='=', command=calculate, width=8, height=3, font=('Poppins', 20),
                          bg='#007acc', fg='white')
equals_button.grid(row=4, column=2, padx=5, pady=5)

clear_button = tk.Button(app, text='Clear', command=clear, width=8, height=3, font=('Poppins', 20),
                         bg='#FF5722', fg='white')
clear_button.grid(row=4, column=0, padx=5, pady=5)


app.mainloop()
