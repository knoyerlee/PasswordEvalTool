from passfunctions import Password 
import tkinter as tk
from tkinter import messagebox
import pyperclip

password1 = Password()

def display_strong_password():
    strong_pass = password1.generate_strong_password()
    messagebox.showinfo(message='The password has been copied to your clipboard')
    pyperclip.copy(strong_pass)

def check_password():
    user_password = eval_password_field.get()
    user_result = password1.check_password(user_password)
    if (user_result):
        messagebox.showinfo(title='Password Results', message='This is a strong password')
    else:
        messagebox.showinfo(title='Password Results', message='This password needs improvment')
    

window = tk.Tk()
# Gets the size of the window and sets the parameters accordingly
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
# Sets the window to be fullscreen
window.geometry(f'{width}x{height}')
window.title("Password Generator")
window.config(bg='#DADED4')

title_frame = tk.Frame(window)
title_frame.config(bg='#A3BCB6', width=width, height=100, highlightbackground='black', highlightthickness=1)
title_frame.pack()

# This prevents the Frame from shrinking
title_frame.pack_propagate(False)

title_frame_content = tk.Label(title_frame)
title_frame_content.config(text="Random Password Generator and Password Eval Tool", bg='#A3BCB6', fg='#000', font=("Arial", 20))
# This is used to center an item in a frame when pack() is used
title_frame_content.pack(fill="none", expand=True)

content_frame = tk.Frame(window)
content_frame.config(bg='#A3BCB6', width=(width - 300), height=500, highlightbackground='black', highlightthickness=1)
content_frame.pack(pady=20)

# Prevents the Frame from shrinking
content_frame.pack_propagate(False)

eval_password_frame = tk.Frame(content_frame)
eval_password_frame.config(bg='#A3BCB6')
eval_password_frame.pack(fill='none', expand=True)

eval_password_label = tk.Label(eval_password_frame)
eval_password_label.config(text="Enter the Password You Would Like Evaluated Below", bg='#A3BCB6')
eval_password_label.pack(pady=5)

eval_password_field = tk.Entry(eval_password_frame)
eval_password_field.config(highlightbackground='#3C403D', highlightthickness=1, width=50, bg='#39603D', fg='#FFF')
eval_password_field.pack()

eval_password_button = tk.Button(eval_password_frame)
eval_password_button.config(text='Evaluate', bg='#39603D', fg='#FFF', command=check_password)
eval_password_button.pack(pady=5)

gen_password_field = tk.Button(content_frame)
gen_password_field.config(text= 'Generate a Password', highlightbackground='#3C403D', highlightthickness=1, bg='#39603D', 
    fg='#FFF', command=display_strong_password)
gen_password_field.pack(fill='none', expand=True)



window.mainloop()
