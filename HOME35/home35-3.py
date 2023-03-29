""" создайте функцию бесконечности 
infinite(list, tries)
for x in infinite([1,2,3], 2):
   print(x)
list= [str('1 2 3 ') for x in range(0,2) ]

print("".join(list))
1 2 3 1 2 3
 """
"""
def infinite( ):
   for x in range(2) :
      print("[1,2,3]")
   return
 
print(infinite())

"""

""" def infinite (list,tries):
   l=[]
   for x in list:
      l.append(x)
      print(l)
   return  
print(infinite([1,2,3],2)) """

def infinite (list,tries):
   l=[x for x in range(1,4)]
   tries=tries-1
   list.extend(l*tries)
   print(list)
     
   return  

print(infinite([1,2,3],2))