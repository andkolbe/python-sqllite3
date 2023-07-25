import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

customers = [('Bob', 'Jungles', 'bobby@aol.com'), ('Sepp', 'Kuss', 'seppyboy@aol.com'), ('Thibout', 'Pinot', 'thibout@aol.com')]

# c.executemany(""" 
# INSERT INTO customers
# VALUES (?, ?, ?)
# """, customers)

c.execute("""
SELECT rowid, * FROM customers
""")

items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()