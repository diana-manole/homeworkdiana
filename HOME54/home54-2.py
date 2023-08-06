from tkinter import *  
  

window = Tk()  
window.title("Добро пожаловать")  
window.geometry('400x250')  
lbl = Label(window, text="Привет", font=("Arial Bold", 15))  
lbl.grid(column=0, row=0)  
btn = Button(window, text="button1 !")  
btn.grid(column=1, row=0)  
def new_win():
    win=Toplevel(window)
    label=Label(win,text="text in top level",font=20)
    label.pack()
    
def exit_app():
    window.destroy()
    
main_menu = Menu(window)
window.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label='File', menu=first_item)
first_item.add_command(label='New',command=new_win)
first_item.add_command(label='Exit',command=exit_app)


second_item = Menu(main_menu,tearoff=1)
main_menu.add_cascade(label='Edit', menu=second_item)
second_item.add_command(label='Item1')
second_item.add_command(label='Item2')
second_item.add_command(label='Item3')
second_item.add_separator()
second_item.add_command(label='Item4')
window.mainloop()