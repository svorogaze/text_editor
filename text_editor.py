import tkinter
from tkinter import filedialog


class FileEditor:
    def __init__(self):
        self.file_name = ''

    def save_as(self):
        self.file_name = filedialog.asksaveasfilename(title="Save file", defaultextension=".txt",
                                                      filetypes=(('txt file', '*.txt'), ('all files', '*.*')))
        if self.file_name:
            self.save()

    def save(self):
        if self.file_name:
            f = open(file=self.file_name, encoding='utf-8', mode='w')
            result = text_label.get('1.0', 'end-1c')
            f.write(result)
            f.close()
        else:
            self.save_as()

    def new(self):
        self.file_name = ''
        text_label.delete('1.0', tkinter.END)

    def open(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if self.file_name:
            f = open(file=self.file_name, encoding='utf-8', mode='r')
            string = f.read()
            text_label.delete('1.0', tkinter.END)
            text_label.insert(1.0, string)
            f.close()


window = tkinter.Tk()
window.geometry('800x600')
window.title('Text Editor')
window.iconphoto(True, tkinter.PhotoImage(file='icon.png'))

txt_file = FileEditor()

text_label = tkinter.Text(width=0, height=0, bg='black', fg='#4bd108', insertbackground='green',
                          font=('Consolas', 12))
text_label.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
scroll = tkinter.Scrollbar(command=text_label.yview)
scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
text_label.config(yscrollcommand=scroll.set)

main_menu = tkinter.Menu(window)
window.config(menu=main_menu)
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=txt_file.open)
file_menu.add_command(label="New", command=txt_file.new)
file_menu.add_command(label="Save", command=txt_file.save)
file_menu.add_command(label='Save As', command=txt_file.save_as)
file_menu.add_command(label='Exit', command=exit)
main_menu.add_cascade(label="File",
                      menu=file_menu)

window.mainloop()
