import sqlite3



# This is for craete user table if not exsits

def createTables():

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute('''
                   
CREATE TABLE IF NOT EXISTS User (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id VARCHAR(255),
        Password VARCHAR(255),
        Level INT,
        Date_of_account_creation DATE,
        isApproved BOOLEAN,
        Name VARCHAR(255),
        Address VARCHAR(255),
        Email VARCHAR(255),
        Phone VARCHAR(255),
        PinCode VARCHAR(255)
    );
                   
   ''')
    


    # This is for craete products table if not exsits

    cursor.execute('''
                   
        CREATE TABLE IF NOT EXISTS Products (
                   
        Products_Id INTEGER PRIMARY KEY AUTOINCREMENT,

        name VARCHAR(255),  
        price FLOAT,             
        category VARCHAR(255),
        certified BOOLEAN,
        stack INTEGER(255)             
             
        )''')
    


     # This is for create order table if not exsits

    cursor.execute('''

            CREATE TABLE IF NOT EXISTS Order_Details(
                   
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255),
                user_name VARCHAR(255),
                user_address VARCHAR(255),
                phone VARCHAR(255),
                product_id VARCHAR(255),
                product_name VARCHAR(255),
                category VARCHAR(255),
                status BOOLEAN,
                isApproved BOOLEAN,
                quantity INT,
                date_of_craete_order DATE,
                total_amount FLOAT
            )

        ''')

    conn.commit()
    conn.close()