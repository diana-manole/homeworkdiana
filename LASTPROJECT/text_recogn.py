

import easyocr
  

def main( text_fname='result.txt'):
    file_path = input("Enter a file name:")
    reader = easyocr.Reader(['ru','en'])
    result= reader.readtext(file_path,detail=0)
    
    
    with open (text_fname, 'w') as file:
         for line in result :
             file.write(f"{line}\n\n")
             
    return f'Result in {text_fname}'
    
    

if __name__ == "__main__":
    main()
