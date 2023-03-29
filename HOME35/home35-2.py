""" создайте функцию бесконечности 
infinite(list, tries)
for x in infinite([1,2,3], 2):
   print(x)

1 2 3 1 2 3"""
#david

def infinite(list, tries):
    
    tries +=1
    list.extend(list)
    
    
    if tries == 5:
        
        return print(list)  
    return infinite(list, tries)

infinite([1,2,3],0)