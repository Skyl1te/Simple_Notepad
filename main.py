import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
menu = tk.Menu(window)



label = tk.Label(text="Разберайся сам, мне лень тебе что-то обьяснять", font=("Times New Roman", 30))
label2 = tk.Label(text="Это типо блокнот", font=("Times New Roman", 30))



def clear():
    label.destroy()
    label2.destroy()



def help_file():
     print("Разберайся сам, мне лень тебе что-то обьяснять")
     label.pack()



def open_file():
    print("Открываем файл!")
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file',
                                           filetypes=(('Text Documents', '*.txt'), ('all files', '*.*'),
                                                      ('Python', '*.py')))
    if file_name:
        f = open(file_name, 'r')
        text_open = f.read()
        if text_open != tk.NONE:
            text.delete(1.0, tk.END)
            text.insert(tk.END, text_open)


def save_file():
    print("Сохраняем файл!")
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Выберите файл",
                                             filetypes=(("текстовые документы", "*.txt"),
                                                        ("все файлы", "*.*"),
                                                        ("Python", "*.py")))
    if file_name:
        f = open(file_name, "a+")
        text_save = str(text.get(1.0, tk.END))
        f.write(text_save + "\n")
        f.close()


def close_file():
    menu = tk._exit()


text = tk.Text(font=("Comic Sans MS", 30), bg="pink")
text.pack(expand=tk.YES, fill=tk.BOTH)


def about():
    print("Это типо блокнот")
    label2.pack()

def new_file():
    text.delete(1.0, tk.END)



window.config(menu=menu)

window.geometry("600x500")

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New file", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save as", command=save_file)
file_menu.add_command(label="Exit", command=close_file)
menu.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu, tearoff=0)

help_menu.add_command(label='Help', command=help_file)
help_menu.add_command(label='About', command=about)
help_menu.add_command(label='Clear fact of programs', command=clear)

menu.add_cascade(label='Help', menu=help_menu)






window.mainloop()
