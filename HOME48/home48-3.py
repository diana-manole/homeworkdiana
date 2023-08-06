
def is_acceptable_password(password: str) -> bool:
    if all(map(str.isdigit, password)) and len(password)> 9:
            return True
    elif 6<len(password) <9 and  any(map(str.isdigit, password)) and any(map(str.isalpha, password)):
            return True
    elif 6<len(password)and len(password)> 9 and all(map(str.isalpha, password)) or any(map(str.isdigit, password))<=1 and len(password)> 9:
            return True
    else:
        return False
            
            
            
print("Example:")
#print(is_acceptable_password("short"))
#print(is_acceptable_password("muchlonger"))
print(is_acceptable_password('1234567'))