class User:
    def __init__(self, first_name, last_name, email, password, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        

class Users: 
    def __init__(self):
        self.users = []
        
    def add_user(self, *users):
        self.users.extend(users)
        
    

class Project:
    def __init__(self, title, details, total_target, start_date, end_date, owner):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner
    
    def is_owner(self, user):
        return self.owner == user
        
    
class projects: 
    def __init__(self):
        self.projects = []
        
    def add_project(self, *projects):
        self.projects.extend(projects)