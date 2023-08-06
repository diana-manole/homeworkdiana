from tkinter import *  
from text_recogn import Recogn
from tkinter import filedialog 
    
window = Tk()  
window.title(" Text Recognition System")  
window.geometry('350x450+70+50') 
window.resizable(width=True,height=True) 
lbl = Label(window, text="Welcome", font=(9),foreground=("black"))  
lbl.pack() 

file=StringVar() 

lbl2=Label(text="Input your file",width=30,height=10)
lbl2.pack()
entry=Entry(textvariable=file)
entry.pack()

def start_action():
    if entry["text"] =="" or entry["text"] ==None:
        wind = tk.TK()
        l = tk.Label(wind,text = "Plese uplod your file for recognitie him")
        l.pack()
        wind.mainloop
    else:
        file = entry["text"]
        Recogn(file).text_reco()


def new_win():
    file =filedialog.askopenfile()
    entry["text"] =file.name
    entry.delete(0,END)
    entry.insert(0,file.name)
    
def exit_app():
    window.destroy()
    
btn = Button(window, text="Go!",width=3,height=2,bg="pink",command=start_action)  
btn.pack()

main_menu = Menu(window)
window.configure(menu=main_menu)
second_item = Menu(main_menu,tearoff=1)
main_menu.add_cascade(label='Help', menu=second_item)
second_item.add_command(label='About')
second_item.add_separator()
second_item.add_command(label='Extra')

def main():
    

    first_item = Menu(main_menu)
    main_menu.add_cascade(label='File', menu=first_item)
    first_item.add_command(label='New',command=new_win)
    first_item.add_command(label='Exit',command=exit_app)

    
    
    window.mainloop()

if __name__=="__main__":
    main()







        