class Contact:
    def __init__(self,firstname= None, lastname= None, middlename= None,  company= None, address= None, homephone= None, mobilephone= None, workphone= None,
                         email= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email