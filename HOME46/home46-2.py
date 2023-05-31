def divisible(num):
    if (num%2)==0:
       return "четное"
    else:
       return "нечетное"
   
print(divisible(-3))
print(divisible(5))
print(divisible(6))



def flip_bool(boolean):
   if boolean == True:
      return False
   else:
      return True
   
print(flip_bool(True))
print(flip_bool(False))
print(flip_bool(1))
print(flip_bool(0))

def google(number):
    return (f"G{number*'o'}gle")
 
print(google(5))

def new_word(word):
    return word[1:]
print(new_word("apple"))

def NOT(num):
   if num ==1:
      return 0
   else:
      return 1
	
 
print(NOT(0))
print(NOT(1))

def AND(num,num2):
   if  num==num2==1:
      return 1
   else:
      return 0
	
print(AND(1,1)) 
print(AND(0,0))

def OR(num,num2):
   if  num==num2==1:
      return 1
   else:
      return 1
   
print(OR(1,0)) 
print(OR(1,1))

def NOT(num):
	return not num

def AND(num,num2):
	return num and num2

def OR(num,num2):
	return num or num2

def calculator(number1, operator, number2):
    if number2==0:
        return ("Нельзя делить на 0!")
    else:
        return()
     
print(calculator(2, "+", 2))