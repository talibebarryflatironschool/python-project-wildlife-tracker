class User:
    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email

    # Getters and setters
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Class methods for database operations
    @classmethod
    def create_table(cls, conn):
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()

    @classmethod
    def create(cls, conn, name, email):
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            user_id = c.lastrowid
            return cls(user_id, name, email)
        except Exception as e:
            print("Error creating user:", e)
            return None

    @classmethod
    def delete(cls, conn, user_id):
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

    @classmethod
    def get_all(cls, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        return [cls(row["id"], row["name"], row["email"]) for row in rows]

    @classmethod
    def find_by_email(cls, conn, email):
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = c.fetchone()
        if row:
            return cls(row["id"], row["name"], row["email"])
        return None

    @classmethod
    def get_by_id(cls, conn, user_id):
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        if row:
            return cls(row["id"], row["name"], row["email"])
        return None

    def __repr__(self):
        return f"<User(id={self._id}, name='{self._name}', email='{self._email}')>"
