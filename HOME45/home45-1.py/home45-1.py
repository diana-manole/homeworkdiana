#1 проверить все ли числа последовательности уникальны

  


""" 
with open('file0.txt', 'r') as f:
    t = f.read()

l=[]

for i in t:
    if i not in l:
        l.append(i)
        
print(l)


 """


with open('file0.txt', 'r') as f:
    t = f.read()

l=[]

for i in t:
    if i % (15):
        l.append(i)
        
print(l)


