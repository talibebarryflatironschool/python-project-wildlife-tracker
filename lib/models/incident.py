class Incident:
    def __init__(self, id, patrol_id, incident_type, description):
        self._id = id
        self._patrol_id = patrol_id
        self._incident_type = incident_type
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def patrol_id(self):
        return self._patrol_id

    @property
    def incident_type(self):
        return self._incident_type

    @incident_type.setter
    def incident_type(self, value):
        self._incident_type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @classmethod
    def create_table(cls, conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patrol_id INTEGER,
                incident_type TEXT,
                description TEXT
            )
        ''')
        conn.commit()

    @classmethod
    def create(cls, conn, patrol_id, incident_type, description):
        c = conn.cursor()
        c.execute("INSERT INTO incidents (patrol_id, incident_type, description) VALUES (?, ?, ?)",
                  (patrol_id, incident_type, description))
        conn.commit()
        incident_id = c.lastrowid
        return cls(incident_id, patrol_id, incident_type, description)

    @classmethod
    def delete(cls, conn, incident_id):
        c = conn.cursor()
        c.execute("DELETE FROM incidents WHERE id = ?", (incident_id,))
        conn.commit()

    @classmethod
    def get_all(cls, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM incidents")
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["incident_type"], row["description"]) for row in rows]

    @classmethod
    def find_by_type(cls, conn, incident_type):
        c = conn.cursor()
        c.execute("SELECT * FROM incidents WHERE incident_type LIKE ?", (f"%{incident_type}%",))
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["incident_type"], row["description"]) for row in rows]

    @classmethod
    def get_by_patrol(cls, conn, patrol_id):
        c = conn.cursor()
        c.execute("SELECT * FROM incidents WHERE patrol_id = ?", (patrol_id,))
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["incident_type"], row["description"]) for row in rows]

    def __repr__(self):
        return f"<Incident(id={self._id}, type='{self._incident_type}', description='{self._description}')>"
