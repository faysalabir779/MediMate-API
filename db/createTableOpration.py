import sqlite3

# This is for creating user table if not exists
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

    # This is for creating products table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            Products_Id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),  
            price FLOAT,             
            category VARCHAR(255),
            certified BOOLEAN,
            stack INTEGER             
        );
    ''')

    # This is for creating order table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Order_Details (
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
            date_of_create_order DATE,
            total_amount FLOAT,
            product_price FLOAT
        );
    ''')

    # This is for creating available products table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Available_Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR(255),
            product_id VARCHAR(255),
            price FLOAT, 
            product_name VARCHAR(255),
            category VARCHAR(255),
            stock INT
        );
    ''')

    # This is for sell history if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sell_History(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sell_id VARCHAR(255),
            user_id VARCHAR(255),
            user_name VARCHAR(255),
            product_id VARCHAR(255),
            product_name VARCHAR(255),
            category VARCHAR(255),
            quantity INT,
            remaining_stock INT,
            date_of_create_order DATE,
            total_amount FLOAT
        );
    ''')

    conn.commit()
    conn.close()
