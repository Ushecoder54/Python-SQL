import sqlite3

connect = sqlite3.connect('customer.db')

connect.execute('''CREATE TABLE CUSTOMER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL);''')

connect.close()

