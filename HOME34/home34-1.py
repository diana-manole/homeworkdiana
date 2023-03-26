""" 1 Напишите декоратор который будет вызывать какую то функцию n раз где n параметр декоратора """


def my_decorator(func) :
    def wrapper(n):
        print('start')
        func(n)
        print('end')
    return wrapper
    
@my_decorator
def my_func(n):
    for i in range(n):
      print(f'Here I am {i}')
    return my_func
my_func(9)