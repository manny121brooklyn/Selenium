import pyodbc


connection = pyodbc.connect('Driver = {SQL Server};'
                        'Server=LAPTOP-99Q93VC4\SQLEXPRESS;'
                        'Database=yt;'
                        'Trusted_connection=yes;')
cursor = connection.cursor()

cursor.execute('select * from customers')
for row in cursor:
    print(row)




