def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("")
