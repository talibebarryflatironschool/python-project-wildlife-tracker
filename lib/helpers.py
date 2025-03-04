# # lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()



from models import conn, initialize_db
from models.user import User
from models.patrol_log import PatrolLog
from models.sighting import WildlifeSighting
from models.incident import Incident
# Initialize the database tables.
initialize_db()

# -------------- User Management --------------
def manage_users():
    while True:
        print("\n--- Manage Users ---")
        print("1. Create a new user")
        print("2. Delete a user")
        print("3. Display all users")
        print("4. Find user by email")
        print("5. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_user_helper()
        elif choice == "2":
            delete_user_helper()
        elif choice == "3":
            display_users_helper()
        elif choice == "4":
            find_user_by_email_helper()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

def create_user_helper():
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")
    user_obj = User.create(conn, name, email)
    if user_obj:
        print(f"User created with ID: {user_obj.id}")
    else:
        print("Failed to create user.")

def delete_user_helper():
    user_id = input("Enter user ID to delete: ")
    try:
        user_id = int(user_id)
    except ValueError:
        print("User ID must be an integer.")
        return
    User.delete(conn, user_id)
    print("User deleted.")

def display_users_helper():
    users = User.get_all(conn)
    if not users:
        print("No users found.")
    else:
        for user_obj in users:
            print(user_obj)

def find_user_by_email_helper():
    email = input("Enter email to search: ")
    user_obj = User.find_by_email(conn, email)
    if user_obj:
        print(user_obj)
    else:
        print("User not found.")

# -------------- Patrol Log Management --------------
def manage_patrol_logs():
    while True:
        print("\n--- Manage Patrol Logs ---")
        print("1. Create a new patrol log")
        print("2. Delete a patrol log")
        print("3. Display all patrol logs")
        print("4. View patrol log details (sightings/incidents)")
        print("5. Find patrol log by location")
        print("6. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_patrol_log_helper()
        elif choice == "2":
            delete_patrol_log_helper()
        elif choice == "3":
            display_patrol_logs_helper()
        elif choice == "4":
            view_patrol_log_details_helper()
        elif choice == "5":
            find_patrol_log_by_location_helper()
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

def create_patrol_log_helper():
    user_id_input = input("Enter user ID for this patrol (or press Enter for default user): ")
    if user_id_input == "":
        default = User.find_by_email(conn, "default@wildlife.org")
        if default is None:
            default = User.create(conn, "Default Ranger", "default@wildlife.org")
    else:
        try:
            user_id_input = int(user_id_input)
        except ValueError:
            print("User ID must be an integer.")
            return
        default = User.get_by_id(conn, user_id_input)
        if not default:
            print("User not found.")
            return

    location = input("Enter patrol location: ")
    notes = input("Enter patrol notes: ")
    patrol = PatrolLog.create(conn, default.id, location, notes)
    print(f"Patrol log created with ID: {patrol.id}")

def delete_patrol_log_helper():
    patrol_id = input("Enter patrol log ID to delete: ")
    try:
        patrol_id = int(patrol_id)
    except ValueError:
        print("Patrol log ID must be an integer.")
        return
    PatrolLog.delete(conn, patrol_id)
    print("Patrol log deleted.")

def display_patrol_logs_helper():
    logs = PatrolLog.get_all(conn)
    if not logs:
        print("No patrol logs found.")
    else:
        for patrol in logs:
            print(patrol)

def view_patrol_log_details_helper():
    patrol_id = input("Enter patrol log ID to view details: ")
    try:
        patrol_id = int(patrol_id)
    except ValueError:
        print("Patrol log ID must be an integer.")
        return
    patrol = PatrolLog.get_by_id(conn, patrol_id)
    if not patrol:
        print("Patrol log not found.")
        return
    print("Patrol Log:", patrol)
    sightings = WildlifeSighting.get_by_patrol(conn, patrol_id)
    incidents = Incident.get_by_patrol(conn, patrol_id)
    if sightings:
        print("Sightings:")
        for s in sightings:
            print(" ", s)
    else:
        print("No sightings for this patrol.")
    if incidents:
        print("Incidents:")
        for i in incidents:
            print(" ", i)
    else:
        print("No incidents for this patrol.")

def find_patrol_log_by_location_helper():
    location = input("Enter location to search for: ")
    logs = PatrolLog.find_by_location(conn, location)
    if logs:
        for patrol in logs:
            print(patrol)
    else:
        print("No patrol logs found for that location.")

# -------------- Wildlife Sighting Management --------------
def manage_sightings():
    while True:
        print("\n--- Manage Wildlife Sightings ---")
        print("1. Create a new wildlife sighting")
        print("2. Delete a wildlife sighting")
        print("3. Display all wildlife sightings")
        print("4. Find wildlife sighting by species")
        print("5. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_sighting_helper()
        elif choice == "2":
            delete_sighting_helper()
        elif choice == "3":
            display_sightings_helper()
        elif choice == "4":
            find_sighting_by_species_helper()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

def create_sighting_helper():
    patrol_id = input("Enter patrol log ID for this sighting: ")
    try:
        patrol_id = int(patrol_id)
    except ValueError:
        print("Patrol log ID must be an integer.")
        return
    species = input("Enter species name: ")
    count = input("Enter count: ")
    try:
        count = int(count)
    except ValueError:
        print("Count must be an integer.")
        return
    status = input("Enter status (healthy, injured, endangered): ")
    sighting_obj = WildlifeSighting.create(conn, patrol_id, species, count, status)
    print(f"Wildlife sighting created with ID: {sighting_obj.id}")

def delete_sighting_helper():
    sighting_id = input("Enter wildlife sighting ID to delete: ")
    try:
        sighting_id = int(sighting_id)
    except ValueError:
        print("Sighting ID must be an integer.")
        return
    WildlifeSighting.delete(conn, sighting_id)
    print("Wildlife sighting deleted.")

def display_sightings_helper():
    sightings_list = WildlifeSighting.get_all(conn)
    if not sightings_list:
        print("No wildlife sightings found.")
    else:
        for sighting_obj in sightings_list:
            print(sighting_obj)

def find_sighting_by_species_helper():
    species = input("Enter species name to search for: ")
    sightings_list = WildlifeSighting.find_by_species(conn, species)
    if sightings_list:
        for sighting_obj in sightings_list:
            print(sighting_obj)
    else:
        print("No sightings found for that species.")

# -------------- Incident Management --------------
def manage_incidents():
    while True:
        print("\n--- Manage Incidents ---")
        print("1. Create a new incident")
        print("2. Delete an incident")
        print("3. Display all incidents")
        print("4. Find incident by type")
        print("5. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_incident_helper()
        elif choice == "2":
            delete_incident_helper()
        elif choice == "3":
            display_incidents_helper()
        elif choice == "4":
            find_incident_by_type_helper()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

def create_incident_helper():
    patrol_id = input("Enter patrol log ID for this incident: ")
    try:
        patrol_id = int(patrol_id)
    except ValueError:
        print("Patrol log ID must be an integer.")
        return
    incident_type = input("Enter incident type (e.g., poaching, illegal logging): ")
    description = input("Enter incident description: ")
    incident_obj = Incident.create(conn, patrol_id, incident_type, description)
    print(f"Incident created with ID: {incident_obj.id}")

def delete_incident_helper():
    incident_id = input("Enter incident ID to delete: ")
    try:
        incident_id = int(incident_id)
    except ValueError:
        print("Incident ID must be an integer.")
        return
    Incident.delete(conn, incident_id)
    print("Incident deleted.")

def display_incidents_helper():
    incidents_list = Incident.get_all(conn)
    if not incidents_list:
        print("No incidents found.")
    else:
        for incident_obj in incidents_list:
            print(incident_obj)

def find_incident_by_type_helper():
    incident_type = input("Enter incident type to search for: ")
    incidents_list = Incident.find_by_type(conn, incident_type)
    if incidents_list:
        for incident_obj in incidents_list:
            print(incident_obj)
    else:
        print("No incidents found for that type.")

def exit_program():
    print("Exiting Wildlife Patrol Tracker. Goodbye!")
    exit()
