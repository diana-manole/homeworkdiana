import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import easyocr
  
class Recogn:
    def __init__(self,file_path) -> None:
        self.file_path=file_path
    
    
    
    def text_reco(self):
        reader = easyocr.Reader(['en'])
        result= reader.readtext(self.file_path,detail=0)
        
        print(result)
        
    
