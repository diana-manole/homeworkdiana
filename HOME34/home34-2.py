"""2 Напишите декоратор который будет созранять результат функции в файл (имя файла - параметр декоратора) """

def my_decorator(func) :
    def wrapper(filename):
        print('start')
        func(filename)
        print('end')
    return wrapper
    
@my_decorator
def run(filename):
    with open(filename, "w") as wrfile:
        wrfile.write(str("result of function"))
        
run("text.txt")