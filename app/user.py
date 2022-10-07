class User:
    ids = ""
    name = ""
    password = ""
    roleID = ""
    
    def __init__(self,ids,name,password,roleID,status):
        self.ids = ids
        self.name = name
        self.password = password
        self.roleID = roleID
        self.status = status
        
    def display(self):
        return "User[ "+ self.ids + ", " +  self.name +", "+ self.password+", "+ self.roleID+", "+ str(self.status)+" ]";