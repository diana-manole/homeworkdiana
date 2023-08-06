from tkinter import *  
#from text_recogn import *
import easyocr
    
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


def new_win():
    win=Toplevel(window)
    get=file.get()
    label=Label(win, text='', font=20)
    label["text"]=get
    label.pack()
    
def exit_app():
    window.destroy()
    
btn = Button(window, text="Go!",width=3,height=2,bg="pink",command=new_win)  
btn.pack()

main_menu = Menu(window)
window.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label='File', menu=first_item)
first_item.add_command(label='New',command=new_win)
first_item.add_command(label='Exit',command=exit_app)

second_item = Menu(main_menu,tearoff=1)
main_menu.add_cascade(label='Help', menu=second_item)
second_item.add_command(label='About',command=new_win)
second_item.add_separator()
second_item.add_command(label='Extra')


def text_reco(file_path,text_fname='result.txt'):
    reader = easyocr.Reader(['ru','en'])
    result= reader.readtext(file_path,detail=0)
    
    with open (text_fname, 'w') as file:
         for line in result :
             file.write(f"{line}\n\n")
             
    return f'Result in {text_fname}'

def main():
    get=file.get()
    file_path = get
    print(text_reco(file_path=file_path, text_fname="read.txt"))
    
if __name__ == "__main__":
    main()





window.mainloop()





        