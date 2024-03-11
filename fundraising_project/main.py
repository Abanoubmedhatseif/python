import models
import functions

users_database = models.Users()
projects_list = models.projects()



#### to populate test data
# user1 = models.User("Michael", "Johnson", "michael@example.com", "password123", "0111111111")
# user2 = models.User("Emma", "Williams", "emma@example.com", "password456", "0122222222")
# user3 = models.User("James", "Brown", "james@example.com", "password789", "0123333333")
# user4 = models.User("Olivia", "Jones", "olivia@example.com", "passwordabc", "01044444444")
# user5 = models.User("menna", "Taylor", "william@example.com", "passwordxyz", "0125555555")
# menna = models.User("merna","abdalla","merna@gmail.com","menna123","01200228840")


# users_database.add_user(user1,user2,user3,user4,user5)
#projects_list.add_project(project1,project2,project3,project4,project5)



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
