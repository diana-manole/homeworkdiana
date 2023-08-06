import easyocr

def text_reco(file_path):
    reader = easyocr.Reader(['ru','en'])
    result= reader.readtext(file_path,detail=0)

    return result


def main():
    file_path = input("Enter a file name:")
    print(text_reco(file_path=file_path))
    
if __name__ == "__main__":
    main()
        
        
        
f = open ("read.txt")
r=print(f.read())