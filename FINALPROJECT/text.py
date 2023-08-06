from tkinter import *  
from text_recognition import *
import easyocr
    
window = Tk()  
window.title(" ")  
window.geometry('250x550')  
lbl = Label(window, text="Привет", font=(15),foreground=("black"))  
lbl.pack() 
 
lbl2=Label(text="Input your file",width=30,height=10)
lbl2.pack()
entry=Entry()
entry.pack()
file=entry.get

def text_reco(file_path):
    reader = easyocr.Reader(['ru','en'])
    result= reader.readtext(file_path,detail=0)
    
    win=Toplevel(window)
    label=Label(win,
                text=result, 
                font=20)
    label.pack()
    
def main():
    file_path = "text1.jpg"
    print(text_reco(file_path=file_path))
    
if __name__ == "__main__":
    main()

    
btn = Button(window, text="Go!",width=3,height=2,bg="pink",command=main)  
btn.pack()
    
def new_win():
    win=Toplevel(window)
    label=Label(win,
                text="", 
                font=20)
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
main_menu.add_cascade(label='Help', menu=second_item)
second_item.add_command(label='About',command=new_win)
second_item.add_separator()
second_item.add_command(label='Extra')
window.mainloop()



        