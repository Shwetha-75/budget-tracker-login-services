class UserModelDisplay:
      def __init__(self,currentUser):
        self.currentUser=currentUser 
      def methodUserObject(self):
            
            model={
                  'first_name':self.currentUser['first_name'],
                  'last_name':self.currentUser['last_name'],
                  'phone':self.currentUser['phone'],
                  'gender':self.currentUser['gender'],
                  'mail':self.currentUser['mail'],
                  'expenditure':self.currentUser['expenditure'] if 'expenditure' in self.currentUser else [],
                  'salary':self.currentUser['salary'] if 'salary' in self.currentUser else 0,
                  'savings':self.currentUser['savings'] if 'savings' in self.currentUser else 0,
                  'expense_amt':self.currentUser['expense_amt'] if 'expense_amt' in self.currentUser else 0
            }
         
            return model 