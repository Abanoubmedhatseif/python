import models
import re
from datetime import datetime
import json

def readDataFromJsonFile(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def saveDataToJsonFile(new_data, filename):
    file = open(filename, 'r')
    try:
        existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    file.close()

    existing_data.append(new_data)
    file = open(filename, 'w')
    json.dump(existing_data, file, indent=4)
    file.close()


def register_user():
    print("Please provide your information to register:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format. Please try again.")
        email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
    phone = input("Mobile Phone (Egyptian number): ")
    while not re.match(r"01[0-2]{1}[0-9]{8}", phone):
        print("Invalid Egyptian phone number. Please try again.")
        phone = input("Mobile Phone (Egyptian number): ")
    print("User registered successfully!")
    
    newUser = models.User(first_name, last_name, email, password, phone)
    print(newUser.to_dict())
    saveDataToJsonFile(newUser.to_dict(), 'userdata.json')


def login():
    users_database = readDataFromJsonFile('userdata.json')
    print("Please login with your credentials:")
    email = input("Email: ")
    password = input("Password: ")

    for user in users_database:
        if  user['email'] == email and user['password'] == password:
            print("Login successful!")
            return user

    print("Sorry ... Invalid email or password.")
    return None


def show_users():
    users_database = readDataFromJsonFile('userdata.json')
    print("List of users:")
    for idx, user in enumerate(users_database, start=1):
        print(f"{idx}. {user['first_name']} {user['last_name']} ({user['email']})")


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_owner(project, user):
        return project["owner"] == user

def create_project(user):
    print("Create a new project:")
    title = input("Title: ")
    details = input("Details: ")
    target_amount = float(input("Target Amount (EGP): "))
    start_date = input("Start Date (YYYY-MM-DD): ")
    while not is_valid_date(start_date):
        print("Invalid date format. Please try again.")
        start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    while not is_valid_date(end_date):
        print("Invalid date format. Please try again.")
        end_date = input("End Date (YYYY-MM-DD): ")
    newProject = models.Project(title, details, target_amount, start_date, end_date, user)
    saveDataToJsonFile(newProject.to_dict(), 'projectdata.json')
    
    
def view_projects(user):
    projects = readDataFromJsonFile('projectdata.json')
    print("\nList of projects:")
    for idx, project in enumerate(projects, start=1):
        if is_owner(project,user):
            print(f"{idx}. {project['title']} (Owned by You)")
        else:
            print(f"{idx}. {project['title']}")




# def edit_project(user, ):
#     projects_list = readDataFromJsonFile('projectdata.json')
#     print("\nEdit projects owned by you:")
#     print("-----------------------------")
#     for idx, project in enumerate(projects_list, start=1):
#         if is_owner(project,user):
#             print(f"{idx}. {project["title"]}")
    
#     while True:
#         choice = input("\nEnter the number of the project you want to edit (0 to cancel): ")
#         if choice == '0':
#             return

#         try:
#             idx = int(choice) - 1
#             project = projects_list[idx]
#             if is_owner(project,user):
#                 print("Select property to edit:")
#                 print("1. Title")
#                 print("2. Details")
#                 print("3. Target Amount")
#                 print("4. Start Date")
#                 print("5. End Date")
#                 option = input("Enter your choice: ")

#                 if option == '1':
#                     project["title"] = input("Enter new title: ")
#                 elif option == '2':
#                     project["details"] = input("Enter new details: ")
#                 elif option == '3':
#                     project["total_target"] = float(input("Enter new target amount (EGP): "))
#                 elif option == '4':
#                     new_start_date = input("Enter new start date (YYYY-MM-DD): ")
#                     while not is_valid_date(new_start_date):
#                         print("Invalid date format. Please try again.")
#                         new_start_date = input("Enter new start date (YYYY-MM-DD): ")
#                     project["start_date"] = new_start_date
#                 elif option == '5':
#                     new_end_date = input("Enter new end date (YYYY-MM-DD): ")
#                     while not is_valid_date(new_end_date):
#                         print("Invalid date format. Please try again.")
#                         new_end_date = input("Enter new end date (YYYY-MM-DD): ")
#                     project["end_date"] = new_end_date
#                 else:
#                     print("Invalid option. Please enter a number between 1 and 5.")
                
#                 print("Project updated successfully!")
#                 return
#             else:
#                 print("You are not the owner of this project.")
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
         
         
def edit_project(user):
    projects_list = readDataFromJsonFile('projectdata.json')
    print("\nEdit projects owned by you:")
    print("-----------------------------")
    for idx, project in enumerate(projects_list, start=1):
        if is_owner(project, user):
            print(f"{idx}. {project['title']}")
    
    while True:
        choice = input("\nEnter the number of the project you want to edit (0 to cancel): ")
        if choice == '0':
            return

        try:
            idx = int(choice) - 1
            project = projects_list[idx]
            if is_owner(project, user):
                print("Select property to edit:")
                print("1. Title")
                print("2. Details")
                print("3. Target Amount")
                print("4. Start Date")
                print("5. End Date")
                option = input("Enter your choice: ")

                if option == '1':
                    new_title = input("Enter new title: ")
                    project["title"] = new_title
                elif option == '2':
                    new_details = input("Enter new details: ")
                    project["details"] = new_details
                elif option == '3':
                    new_target_amount = float(input("Enter new target amount (EGP): "))
                    project["target_amount"] = new_target_amount
                elif option == '4':
                    new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                    while not is_valid_date(new_start_date):
                        print("Invalid date format. Please try again.")
                        new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                    project["start_date"] = new_start_date
                elif option == '5':
                    new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                    while not is_valid_date(new_end_date):
                        print("Invalid date format. Please try again.")
                        new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                    project["end_date"] = new_end_date
                else:
                    print("Invalid option. Please enter a number between 1 and 5.")
                    continue  # Continue the loop to prompt for choice again
                
                # Update the project in the list
                projects_list[idx] = project
                
                # Save the updated projects list back to the file
                with open('projectdata.json', 'w') as file:
                    json.dump(projects_list, file, indent=4)
                
                print("Project updated successfully!")
                return
            else:
                print("You are not the owner of this project.")
        except IndexError:
            print("Invalid project number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
   
def delete_project(user):
    projects_list = readDataFromJsonFile('projectdata.json')
    print("Delete projects owned by you:")
    for idx, project in enumerate(projects_list, start=1):
        if is_owner(project,user):
            print(f"{idx}. {project["title"]}")
    
    while True:
        choice = input("Enter the number of the project you want to delete (0 to cancel): ")
        if choice == '0':
            return

        try:
            idx = int(choice) - 1
            project = projects_list[idx] 
            if is_owner(project,user):
                confirmation = input(f"Are you sure you want to delete '{project["title"]}'? (yes/no): ")
                if confirmation.lower() == 'yes':
                    del projects_list[idx]
                    print("Project deleted successfully!")
                    return 
                elif confirmation.lower() == 'no':
                    print("Deletion canceled.")
                    return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("You are not the owner of this project.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def search_project_by_date():
    projects_list = readDataFromJsonFile('projectdata.json')
    date_type = input("Do you want to search by project start date or end date? (start/end): ").lower()
    if date_type not in ['start', 'end']:
        print("Invalid input. Please enter 'start' or 'end'.")
        return
    
    date_str = input(f"Enter the date (YYYY-MM-DD) to search for projects by {date_type} date: ")
    try:
        search_date = datetime.strptime(date_str, '%Y-%m-%d')
        found_projects = []
        for project in projects_list:
            project_date = datetime.strptime(project["start_date"] if date_type == 'start' else project["end_date"], '%Y-%m-%d')
            if project_date == search_date:
                found_projects.append(project)
        
        if found_projects:
            print("Projects found:")
            for project in found_projects:
                print(f"{project["title"]} ({'Start' if date_type == 'start' else 'End'} Date: {date_str})")
        else:
            print(f"No projects found for the given {date_type} date.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")