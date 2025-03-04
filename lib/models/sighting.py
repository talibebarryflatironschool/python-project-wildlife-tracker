class WildlifeSighting:
    def __init__(self, id, patrol_id, species, count, status):
        self._id = id
        self._patrol_id = patrol_id
        self._species = species
        self._count = count
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def patrol_id(self):
        return self._patrol_id

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @classmethod
    def create_table(cls, conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS wildlife_sightings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patrol_id INTEGER,
                species TEXT,
                count INTEGER,
                status TEXT
            )
        ''')
        conn.commit()

    @classmethod
    def create(cls, conn, patrol_id, species, count, status):
        c = conn.cursor()
        c.execute("INSERT INTO wildlife_sightings (patrol_id, species, count, status) VALUES (?, ?, ?, ?)",
                  (patrol_id, species, count, status))
        conn.commit()
        sighting_id = c.lastrowid
        return cls(sighting_id, patrol_id, species, count, status)

    @classmethod
    def delete(cls, conn, sighting_id):
        c = conn.cursor()
        c.execute("DELETE FROM wildlife_sightings WHERE id = ?", (sighting_id,))
        conn.commit()

    @classmethod
    def get_all(cls, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM wildlife_sightings")
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["species"], row["count"], row["status"]) for row in rows]

    @classmethod
    def find_by_species(cls, conn, species):
        c = conn.cursor()
        c.execute("SELECT * FROM wildlife_sightings WHERE species LIKE ?", (f"%{species}%",))
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["species"], row["count"], row["status"]) for row in rows]

    @classmethod
    def get_by_patrol(cls, conn, patrol_id):
        c = conn.cursor()
        c.execute("SELECT * FROM wildlife_sightings WHERE patrol_id = ?", (patrol_id,))
        rows = c.fetchall()
        return [cls(row["id"], row["patrol_id"], row["species"], row["count"], row["status"]) for row in rows]

    def __repr__(self):
        return f"<WildlifeSighting(id={self._id}, species='{self._species}', count={self._count}, status='{self._status}')>"
