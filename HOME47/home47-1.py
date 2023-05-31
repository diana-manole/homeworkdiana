"""Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. 
Но есть несколько важных условий:

Начальный и конечный маркеры всегда разные
Если нет начального маркера, то началом считать начало строки
Если нет конечного маркера, то концом считать конец строки
Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
Если конечный маркер стоит перед начальным, то вернуть пустую строку
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
    
Output: Строка."""
""" def between_markers(text: str, begin: str, end: str) -> str:
    try:
        b=text.find(begin)
        e=text.find(end)
        t=text[b+len(begin):e]
        return(t)
    except: 
        if begin and end not in text:
            print(text)
        if text.index(begin) > (text.index(end)):
            print(text)
     

     """
def between_markers(text: str, begin: str, end: str) -> str:
    b=text.find(begin)
    e=text.find(end)
    if b >=0 and e >=0:
        t=text[b+len(begin):e]
        return (t)
    elif b ==-1 and e ==-1:
       return text
    elif b ==-1:
        return (text[:e])
    elif e ==-1:
       return (text[b+len(begin):])
    else:
      return ""
          

print("Example:")
#print(between_markers("What is >apple<", ">", "<"))
#print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))
#print(between_markers("No[/b] hi", "[b]", "[/b]") )
#print(between_markers("No [b]hi", "[b]", "[/b]") )
print(between_markers("Never send a human to do a machine's job.", 'Never', 'do'))
#print(between_markers("No <hi>", ">", "<"))