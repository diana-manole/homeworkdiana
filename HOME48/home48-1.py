""" def is_acceptable_password(password: str) -> bool:
     if len(password) >6:
        return True
     else:
         return False
    
print("Example:")
print(is_acceptable_password("short")) """

def first_word(text: str) -> str:
    a=text.split()
    return a[0]


print("Example:")
print(first_word("Hello world"))


def checkio(num: int) -> str:
    # your code here
    if num%3==0:
        return"Fizz"
    elif num%5==0:
        return"Buzz"
    elif num%5==0:
        return"Buzz"
    else:
        return str(num)
    
    
def is_acceptable_password(password: str) -> bool:
     if len(password) >6:
        if password.isdigit():
            print( True)
        elif len(password) >6:
             print( True)
        else:
            print( False)
