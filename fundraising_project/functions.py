import models
import re
from datetime import datetime


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
    return models.User(first_name, last_name, email, password, phone)


def login(users_database):
    print("Please login with your credentials:")
    email = input("Email: ")
    password = input("Password: ")

    for user in users_database.users:
        if user.email == email and user.password == password:
            print("Login successful!")
            return user

    print("Sorry ... Invalid email or password.")
    return None


def show_users(users_database):
    print("List of users:")
    for idx, user in enumerate(users_database.users, start=1):
        print(f"{idx}. {user.first_name} {user.last_name} ({user.email})")
        


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
    return models.Project(title, details, target_amount, start_date, end_date)

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def view_projects(user, projects):
    print("\nList of projects:")
    for idx, project in enumerate(projects.projects, start=1):
        if project.is_owner(user):
            print(f"{idx}. {project.title} (Owned by You)")
        else:
            print(f"{idx}. {project.title}")


def edit_project(user, projects_list):
    print("\nEdit projects owned by you:")
    print("-----------------------------")
    for idx, project in enumerate(projects_list.projects, start=1):
        if project.is_owner(user):
            print(f"{idx}. {project.title}")
    
    while True:
        choice = input("\nEnter the number of the project you want to edit (0 to cancel): ")
        if choice == '0':
            return

        try:
            idx = int(choice) - 1
            project = projects_list.projects[idx]
            if project.is_owner(user):
                print("Select property to edit:")
                print("1. Title")
                print("2. Details")
                print("3. Target Amount")
                print("4. Start Date")
                print("5. End Date")
                option = input("Enter your choice: ")

                if option == '1':
                    project.title = input("Enter new title: ")
                elif option == '2':
                    project.details = input("Enter new details: ")
                elif option == '3':
                    project.total_target = float(input("Enter new target amount (EGP): "))
                elif option == '4':
                    new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                    while not is_valid_date(new_start_date):
                        print("Invalid date format. Please try again.")
                        new_start_date = input("Enter new start date (YYYY-MM-DD): ")
                    project.start_date = new_start_date
                elif option == '5':
                    new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                    while not is_valid_date(new_end_date):
                        print("Invalid date format. Please try again.")
                        new_end_date = input("Enter new end date (YYYY-MM-DD): ")
                    project.end_date = new_end_date
                else:
                    print("Invalid option. Please enter a number between 1 and 5.")
                
                print("Project updated successfully!")
                return
            else:
                print("You are not the owner of this project.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
def delete_project(user, projects_list):
    print("Delete projects owned by you:")
    for idx, project in enumerate(projects_list.projects, start=1):
        if project.is_owner(user):
            print(f"{idx}. {project.title}")
    
    while True:
        choice = input("Enter the number of the project you want to delete (0 to cancel): ")
        if choice == '0':
            return

        try:
            idx = int(choice) - 1
            project = projects_list.projects[idx] 
            if project.is_owner(user):
                confirmation = input(f"Are you sure you want to delete '{project.title}'? (yes/no): ")
                if confirmation.lower() == 'yes':
                    del projects_list.projects[idx]
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

def search_project_by_date(projects_list):
    date_type = input("Do you want to search by project start date or end date? (start/end): ").lower()
    if date_type not in ['start', 'end']:
        print("Invalid input. Please enter 'start' or 'end'.")
        return
    
    date_str = input(f"Enter the date (YYYY-MM-DD) to search for projects by {date_type} date: ")
    try:
        search_date = datetime.strptime(date_str, '%Y-%m-%d')
        found_projects = []
        for project in projects_list.projects:
            project_date = datetime.strptime(project.start_date if date_type == 'start' else project.end_date, '%Y-%m-%d')
            if project_date == search_date:
                found_projects.append(project)
        
        if found_projects:
            print("Projects found:")
            for project in found_projects:
                print(f"{project.title} ({'Start' if date_type == 'start' else 'End'} Date: {date_str})")
        else:
            print(f"No projects found for the given {date_type} date.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")