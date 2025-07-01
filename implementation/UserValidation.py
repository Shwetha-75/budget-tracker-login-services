from implementation.UserValidationService import UserValidationService
import requests
class UserValidation(UserValidationService):
        def __init__(self):
             
                self.currentUser=None 
                self.doc=None 
        def userValidate(self,mail:dict): 
            return requests.post(f'http://localhost:7006/fetch/{mail}').json()   
            
        
        def validateUser(self,dataModel:dict)->bool:
                self.doc=self.userValidate(dataModel['mail']) 
                
                if self.doc['status']=='no':
                        return False 
                if dataModel['password'] == self.doc['data_model']['password']:
                   self.currentUser=self.doc['data_model']
                   print(self.doc['data_model'])
                   return True 
                return False 
                