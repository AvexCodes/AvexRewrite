import sqlite3
from Database.DBUtils import updateUser
sql = """
        CREATE TABLE `users` (
	        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
	        `discord_id` VARCHAR(18),
	        `tier` INTEGER
        );
      """

conn = sqlite3.connect("database.db")
c = conn.cursor()
#c.execute(sql)

sqla = """
        INSERT into users(discord_id, tier) VALUES(?, ?)
       """

#c.execute(sqla, (686846374737739797, 4,))
#conn.commit()

sql = """
        SELECT * FROM users
      """

rows = c.execute(sql)
rows = rows.fetchall()

for row in rows:
        print(row)

sql = """
        SELECT * FROM users WHERE discord_id = ?
      """    
#r = c.execute(sql, ("402594405585911809",))
#r = r.fetchone()
#print(r)

sql = """
        
      """