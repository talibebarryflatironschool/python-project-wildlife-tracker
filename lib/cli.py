# # lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()




from helpers import (
    manage_users,
    manage_patrol_logs,
    manage_sightings,
    manage_incidents,
    exit_program
)

def main_menu():
    print("\n=== Wildlife Patrol Tracker ===")
    print("1. Manage Users")
    print("2. Manage Patrol Logs")
    print("3. Manage Wildlife Sightings")
    print("4. Manage Incidents")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            manage_users()
        elif choice == "2":
            manage_patrol_logs()
        elif choice == "3":
            manage_sightings()
        elif choice == "4":
            manage_incidents()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
