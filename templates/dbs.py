import mysql.connector
import pandas as pd
import pyodbc


data = pd.read_csv('zomato_res.csv')

df = pd.DataFrame(data)

print(df)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      "Server=cd C:\Program Files\MySQL\MySQL Server 8.0\bin;"
                      'Database=rok;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('CREATE TABLE people_info (Name nvarchar(50), Country nvarchar(50), Age int)')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.people_info (Name, Country, Age)
                VALUES (?,?,?)
                ''',
                row.Name, 
                row.Country,
                row.Age
                )
conn.commit()