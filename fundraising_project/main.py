import models
import functions

users_database = models.Users()
projects_list = models.projects()

logged_in_user = None

while True:
    print("\nOptions:")
    if logged_in_user:
        print("1. Show active Projects")
        print("2. Create a project")
        print("3. Edit Projects")
        print("4. delete a Project")
        print("5. Search projects by date")
        print("6. Logout")
        print("7. Exit")
    else:
        print("1. Login")
        print("2. Register")
        print("3. Show Users")
        print("4. Exit")

    choice = input("Enter your choice: ")

    if not logged_in_user:
        if choice == '1':
            logged_in_user = functions.login()
        elif choice == '2':
            newUser = functions.register_user()
            users_database.add_user(newUser)
        elif choice == '3':
            functions.show_users()
        elif choice == '4':
            print("Exiting program...\n")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    else:
        if choice == '1':
            functions.view_projects(logged_in_user)
        elif choice == '2':
            functions.create_project(logged_in_user)
        elif choice == '3':
            functions.edit_project(logged_in_user)
        elif choice == '4':
            functions.delete_project(logged_in_user)
        elif choice == '5':
            functions.search_project_by_date()
        elif choice == '6':
            logged_in_user = None
            print("Logged out successfully.")
        elif choice == '7':
            print("Logging out ...")
            print("Exiting program...\n")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
