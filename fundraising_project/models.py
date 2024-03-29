class User:
    def __init__(self, first_name, last_name, email, password, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
    
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone
        }
        
    

class Project:
    def __init__(self, title, details, total_target, start_date, end_date, owner):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner
        
    def to_dict(self):
        return {
            "title": self.title,
            "details": self.details,
            "total_target": self.total_target,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "owner": self.owner
        }
    
    def is_owner(self, user):
        return self.owner == user
        
