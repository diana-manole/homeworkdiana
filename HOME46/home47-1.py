def goes_after(word: str, first: str, second: str) -> bool:
     for i in word:
            if i==first:
              return True
            else :
                return False
            
    


print("Example:")
print(goes_after("world", "w", "o"))