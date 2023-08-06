import easyocr

def text_reco(file_path,text_fname='result.txt'):
    reader = easyocr.Reader(['ru','en'])
    result= reader.readtext(file_path,detail=0)
    
    with open (text_fname, 'w') as file:
         for line in result :
             file.write(f"{line}\n\n")
             
    return f'Result in {text_fname}'

def main():
    file_path = input("Enter a file name:")
    print(text_reco(file_path=file_path, text_fname="read.txt"))
    
if __name__ == "__main__":
    main()
