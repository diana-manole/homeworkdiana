""" 1 Создать класс мобильник - создать несколько жкземпляров со случакйными номерами
в классе конструктор сохраняет номер телефона
метод включить - печатает номер - "включен" и метод выключить - печатает выкелючен
включать выключать  """

from random import randint


class Mobile:
    
    def __init__(self,phone_number) -> None:
        self.phone_number=phone_number
        
        
    def save_number(self,phone_number):
        list=[]
        list.append(randint(0,10)) 
        list=phone_number  
                  
        return
    
    def on(self,phone_number):
        print(f'{phone_number} is on')
        return

    def off(self):
        return print("is on,on,off")
    
Ann=Mobile(phone_number=list)
print(Ann)

