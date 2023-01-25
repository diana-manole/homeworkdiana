class GetFromApi():
    
    def __init__(self,baseURL)->None:
        self.baseURL=baseURL
        
    def addMethod(self, method:str, patameters:dict):
        self.URL=""
        if self.baseURL[-1]!="/":
            self.URL=self.baseURL+'/'
        else:
            self.URL=self.baseURL
        self.URL=self.URL +method
 #       {
 #      [parameter1 name]:value,
 #      [parameterc name]:value,
 #        }    
            
       