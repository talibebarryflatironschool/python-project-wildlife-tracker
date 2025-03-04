from datetime import datetime

class PatrolLog:
    def __init__(self, id, user_id, date_time, location, notes):
        self._id = id
        self._user_id = user_id
        self._date_time = date_time
        self._location = location
        self._notes = notes

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def date_time(self):
        return self._date_time

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value

    @classmethod
    def create_table(cls, conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS patrol_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date_time TEXT,
                location TEXT,
                notes TEXT
            )
        ''')
        conn.commit()

    @classmethod
    def create(cls, conn, user_id, location, notes, date_time=None):
        if date_time is None:
            date_time = datetime.utcnow().isoformat()
        c = conn.cursor()
        c.execute("INSERT INTO patrol_logs (user_id, date_time, location, notes) VALUES (?, ?, ?, ?)",
                  (user_id, date_time, location, notes))
        conn.commit()
        patrol_id = c.lastrowid
        return cls(patrol_id, user_id, date_time, location, notes)

    @classmethod
    def delete(cls, conn, patrol_id):
        c = conn.cursor()
        c.execute("DELETE FROM patrol_logs WHERE id = ?", (patrol_id,))
        conn.commit()

    @classmethod
    def get_all(cls, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM patrol_logs")
        rows = c.fetchall()
        return [cls(row["id"], row["user_id"], row["date_time"], row["location"], row["notes"]) for row in rows]

    @classmethod
    def find_by_location(cls, conn, location):
        c = conn.cursor()
        c.execute("SELECT * FROM patrol_logs WHERE location LIKE ?", (f"%{location}%",))
        rows = c.fetchall()
        return [cls(row["id"], row["user_id"], row["date_time"], row["location"], row["notes"]) for row in rows]

    @classmethod
    def get_by_id(cls, conn, patrol_id):
        c = conn.cursor()
        c.execute("SELECT * FROM patrol_logs WHERE id = ?", (patrol_id,))
        row = c.fetchone()
        if row:
            return cls(row["id"], row["user_id"], row["date_time"], row["location"], row["notes"])
        return None

    def __repr__(self):
        return f"<PatrolLog(id={self._id}, location='{self._location}', date_time='{self._date_time}')>"
