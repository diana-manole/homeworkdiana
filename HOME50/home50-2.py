def beginning_zeros(a: str) -> int:
    # your code here
    num = 0
    for x in a:
        if int(x)==0:
          num +=1
        else:
          return num
    return num
 

print("Example:")
print(beginning_zeros("0010"))