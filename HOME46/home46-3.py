def calculator(number1, operator, number2):
    if number2==0:
        return ("Нельзя делить на 0!")
    else:
        return(number1 and int(operator) and number2)
     
#print(calculator(2, "+", 2))

#print(type(int("+")))


def should_serve_drinks(age, on_break):
    if age>=18 and on_break==False:
        return True
    else:
        return False
    
    
def inches_to_feet(inches):
    if inches<=12:
        return 0
    else:
	    return inches/12

print(inches_to_feet(12))