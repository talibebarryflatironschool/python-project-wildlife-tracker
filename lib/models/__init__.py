# import sqlite3

# CONN = sqlite3.connect('wildlife_tracker.db')
# CURSOR = CONN.cursor()



import sqlite3

# Establish connection to the SQLite database file.
conn = sqlite3.connect("wildlife_patrol_tracker.db")
conn.row_factory = sqlite3.Row  # Enables dictionary-like access to rows.

def initialize_db():
    from .user import User
    from .patrol_log import PatrolLog
    from .sighting import WildlifeSighting
    from .incident import Incident

    User.create_table(conn)
    PatrolLog.create_table(conn)
    WildlifeSighting.create_table(conn)
    Incident.create_table(conn)
