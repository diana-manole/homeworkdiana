""" 2. Садовник и помидоры
Классовая структура
Предлагаем создать следующую классовую структуру: 

Есть Помидор со следующими характеристиками: 
Индекс
Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
Помидор может: 
Расти (переходить на следующую стадию созревания)
Предоставлять информацию о своей зрелости

Есть Куст с помидорами, который: 
Содержит список томатов, которые на нем растут
И может: 
Расти вместе с томатами
Предоставлять информацию о зрелости всех томатов
Предоставлять урожай

И также есть Садовник, который имеет: 
Имя
Растение, за которым он ухаживает
И может: 
Ухаживать за растением
Собирать с него урожай """

class tomato() :
    def __init__(self,index,stage,time) :
        self.index = index
        self.stage = stage
        self.time = time
        
    def ripeness (self) :
        if self.time =='March':
           print(f'{self.index} is on {self.stage[0]} stage')
        if self.time =='May':
           print(f'{self.index} is on {self.stage[1]} stage')
        if self.time =='July':
           print(f'{self.index} is on {self.stage[2]} stage')
        if self.time =='August':
           print(f'{self.index} is on {self.stage[3]} stage')
           
    def shrub(self,name,kind) :
        self.name = name
        self.kind = kind
    
            
    
    def gardener(self,name,plant,pick_time) :
        self.name = name
        self.plant = plant
        self.pick_time = pick_time
        
        
        
n=int(input())
r=map(lambda x:x*n in range(1,n-1))
print(r)