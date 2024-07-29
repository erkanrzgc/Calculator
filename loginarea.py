# StringVar to hold the text input
input_text = tk.StringVar()

# Giriş alanı çerçevesi
input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

# Giriş alanı
input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
