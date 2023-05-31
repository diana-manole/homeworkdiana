""" def checkio(data):
    n= (1, 5, 10, 50, 100, 500, 1000)
    l= ('I', 'V', 'X', 'L', 'C', 'D', 'M')	 
    
    for i in range (n):
        return i.index[i]==l.index
    #replace this for solution
    return ""

print(checkio(5))
"""  
romans= (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1)) 



num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman

