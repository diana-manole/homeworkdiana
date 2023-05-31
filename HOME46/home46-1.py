def hello_world():
    return ("Привет, Мир!") 

print(hello_world())


def addition(a, b):
    return (a+b)

print(addition(3, 3))
print(addition(-1, 5))
print(addition(20, 1))


def addition(number):
    return (number+1)
print(addition(0))
print(addition(10))
print(addition(-2))


def convert_minutes_2_seconds(minutes):
    return (minutes*60)
print(convert_minutes_2_seconds(1))
print(convert_minutes_2_seconds(2))
print(convert_minutes_2_seconds(0))


def triangle_area(base, height):
     return (base*height)/2
    
print (triangle_area(3, 2))



def convert_hours_2_seconds(hours):
    return hours*3600

print(convert_hours_2_seconds(1))



def convert_age_2_days(years):
    return years*365

print(convert_age_2_days(65))


def remainder(x, y):
    return x%y