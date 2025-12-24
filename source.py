import sqlite3



conn = sqlite3.connect("source.db")

cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INTEGER,                
                 email  TEXT UNIQUE
)
""")

users = [("james",24,"james@email.com"),("mila",25,"milatwantwa522@yahoo.com"),
         ("siya",25,"siyangcebetsha544@yahoo.com"),("mazibuko",24,"madolomazizi78@"),
         ("kaka",45,"kakazaza56@gmail.com")

]
cursor.executemany("""INSERT INTO users(name,age,email)
               VALUES (?,?,?)
""",users)

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

