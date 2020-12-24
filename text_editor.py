import tkinter
from tkinter import filedialog


def save_as():
    global file_name
    file_name = filedialog.asksaveasfilename(title="Save file", defaultextension=".txt",
                                             filetypes=(('txt file', '*.txt'), ('all files', '*.*')))
    if file_name:
        f = open(file=file_name, encoding='utf-8', mode='w')
        result = text_label.get('1.0', 'end-1c')
        f.write(result)
        f.close()


def save():
    global file_name
    if file_name:
        f = open(file=file_name, encoding='utf-8', mode='w')
        result = text_label.get('1.0', 'end-1c')
        f.write(result)
        f.close()
    else:
        save_as()


def new():
    global file_name
    file_name = ''
    text_label.delete('1.0', tkinter.END)


def open_f():
    global file_name
    file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    file = open(file=file_name, encoding='utf-8', mode='r')
    string = file.read()
    text_label.delete('1.0', tkinter.END)
    text_label.insert(1.0, string)
    file.close()


window = tkinter.Tk()
window.geometry('800x600')
window.title('Python text editor')
window.iconphoto(True, tkinter.PhotoImage(file='icon.png'))
name = None
file_name = ''

text_label = tkinter.Text(width=0, height=0, bg='black', fg='#4bd108', insertbackground='green',
                          font=('Consolas', 12))
text_label.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
scroll = tkinter.Scrollbar(command=text_label.yview)
scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
text_label.config(yscrollcommand=scroll.set)

mainmenu = tkinter.Menu(window)
window.config(menu=mainmenu)
filemenu = tkinter.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Open", command=open_f)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label='Save As', command=save_as)
filemenu.add_command(label='Exit', command=exit)
mainmenu.add_cascade(label="File",
                     menu=filemenu)

window.mainloop()
