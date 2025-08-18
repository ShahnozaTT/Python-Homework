# # Homework

# ### Review Exercises

# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
# 2.  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |


# 3. Update the Name of Jadzia Dax to be Ezri Dax


# 4.  Display the Name and Age of everyone in the table classified as Bajoran.


import sqlite3

conn = sqlite3.connect("Roster.db")
cursor = conn.cursor()

# создаём таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# вставляем данные
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", 
            ('Benjamin Sisko', 'Human', 40))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", 
            ('Jadzia Dax', 'Trill', 300))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", 
            ('Kira Nerys', 'Bajoran', 29))

# обновляем Jadzia → Ezri
cursor.execute("""
UPDATE Roster
SET Name = ?
WHERE Name = ?
""", ('Ezri Dax', 'Jadzia Dax'))

# сохраняем изменения
conn.commit()

# выборка Bajoran
print("Bajoran персонажи:")
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ('Bajoran',))
for row in cursor.fetchall():
    print(row)

# вывод всей таблицы
print("\nВся таблица Roster:")
cursor.execute("SELECT * FROM Roster")
for row in cursor.fetchall():
    print(row)

conn.close()





