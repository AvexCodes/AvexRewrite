import sqlite3 as mysql
from Utils.Cache import tiers_cache, appendTiers

conn = mysql.connect('database.db')
c = conn.cursor()

def getUserTier(id):
    if id in tiers_cache:
        tier = tiers_cache[id]
    else:
        conn = mysql.connect("database.db")
        c = conn.cursor()

        r = c.execute("SELECT * FROM users WHERE discord_id = ?", (id,))
        r = r.fetchone()

        if r is None:
            return "User"
            appendTiers(str(id), 1)
        
        tier = r[2]
        appendTiers(str(id), tier)
        

    if tier == 0:
        return "Blocked"
    elif tier == 1:
        return "User"
    elif tier == 2:
        return "Donator"
    elif tier == 3:
        return "Support"
    elif tier == 4:
        return "Developer"


def isUserDeveloper(id: str = None):
    if id is None:
        return False
    if id in tiers_cache:
        row = tiers_cache[id]
    else:
        sql = """
                SELECT * FROM users WHERE discord_id = ?
            """
        
        row = c.execute(sql, (id,))
        
        row = row.fetchone()
        if row is None:
            return False
            appendTiers(str(id), 1)
        row = row[2]
        appendTiers(str(id), row)
    
    sql = ""
    if row >= 4: return True
    else: return False

def updateUser(id: str, rank: int):
    # python your a wanker
    if id in tiers_cache:
        tiers_cache[id] = rank

    sql = """
            SELECT * FROM users WHERE discord_id = ?
          """
    r = c.execute(sql, (id,))
    r = r.fetchone()
    if r is None:
        sql = """
                INSERT INTO users(discord_id, tier) VALUES(?,?)
              """
        c.execute(sql, (id, rank,))
        conn.commit()
    
    sql = """   
            UPDATE users SET tier = ? WHERE discord_id = ?
          """
    c.execute(sql, (rank, id,))
    conn.commit()
    
def isUserBlocked(id: str=None):
    sql = """
          SELECT * FROM users WHERE discord_id = ?
          """
    
    r = c.execute(sql, (id,))
    r = r.fetchone()
    if r is None:
        tiers_cache[id] = 1
        return False
    
    tiers_cache[id] = r[2]

    if r[2] == 0:
        return True
    else: return False

def isUserSupport(id: str):
    if id is None:
        return False
    if id in tiers_cache:
        row = tiers_cache[id]
    else:
        sql = """
                SELECT * FROM users WHERE discord_id = ?
            """
        
        row = c.execute(sql, (id,))
        
        row = row.fetchone()
        if row is None:
            return False
            appendTiers(str(id), 1)
        row = row[2]
        appendTiers(str(id), row)
    
    sql = ""
    if row >= 3: return True
    else: return False