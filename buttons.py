# Buton çerçevesi
button_frame = tk.Frame(window, width=400, height=350, bg="grey")
button_frame.pack()

# Butonları ekleme
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row = 0
col = 0
for button in buttons:
    action = lambda x=button: button_click(x)
    if button == "C":
        action = button_clear
    elif button == "=":
        action = button_equal

    tk.Button(button_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=action).grid(row=row, column=col, padx=1, pady=1)
    col += 1
    if col > 3:
        col = 0
        row += 1
