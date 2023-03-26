""" 1 Создать класс (наследник потока) который в потоке будет читать файл и считать количество слов
сделайте так что этот класс запускается start и основной  поток приложения продолжает выводить на экран данные просто какие то выводы """

from threading import Thread
from time import sleep

class readfile(Thread):
    def __init__(self,filename):
        Thread.__init__(self)
        self.fi = filename
        
    def replace( self ,filename):
        print(f'process {filename}')
        with open(filename, 'r') as f:
            content = f.read()
        content = ''.join ([x for x in content if x.isalpha() or x == ' '])
        content = content.split()
        #return [content.lower(),1]
        
                   
readfile()        
        
mythread = readfile("advs.txt")
mythread.start()