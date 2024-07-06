import sqlite3
import uuid
from datetime import date




    # This is for creating new user in the database
 
def createUser(Name, Password, Address, Email, Phone, PinCode):
    try:
        conn = sqlite3.connect("my_medicalShop.db")
        cursor = conn.cursor()

        dataOfCreation = date.today()
        user_id = str(uuid.uuid4())

        cursor.execute("""
            INSERT INTO User (User_id, Password, Level, Date_of_account_creation, isApproved, Name, Address, Email, Phone, PinCode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, Password, -1, dataOfCreation, "", Name, Address, Email, Phone, PinCode))

        conn.commit()
        conn.close()

        return user_id

    except Exception as e:
        raise ValueError("User creation failed: " + str(e))
    






# This is for add new products in the database

def add_product(name, price, category, stack,certified):

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO Products (name, price, category, stack,certified)
    VALUES (?, ?, ?, ?,?)

    """, (name, price, category, stack,certified))
    
    conn.commit()
    conn.close()


                            
def available_order(user_id, product_id, price, product_name, category, stock):

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO Available_Products (user_id, product_id, price, product_name,category, stock)
    VALUES (?, ?, ?, ?,?,?)

    """, (user_id, product_id, price, product_name,category, stock))
    
    conn.commit()
    conn.close()




# This is for add order details

def order_details(user_id, user_Name, user_address, phone, product_id, product_Name, category, status, total_amount, quantity, product_price):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    date_of_create_order = date.today()

    cursor.execute("""

            INSERT INTO Order_Details (user_id, user_name, user_address, phone, product_id, product_name, category, status, isApproved, quantity, date_of_create_order, total_amount, product_price)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (user_id, user_Name, user_address, phone, product_id, product_Name, category, status, "" ,quantity, date_of_create_order, total_amount, product_price))

    conn.commit()
    conn.close()
    

def sell_history(user_id, user_name, product_id, product_name, category, quantity, remaining_stock, total_amount):
    try:
        conn = sqlite3.connect("my_medicalShop.db")
        cursor = conn.cursor()

        dataOfCreation = date.today()
        sell_id = str(uuid.uuid4())

        cursor.execute("""
            INSERT INTO Sell_History(sell_id, user_id, user_name, product_id, product_name, category, quantity, remaining_stock, date_of_create_order, total_amount)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (sell_id, user_id, user_name, product_id, product_name, category, quantity, remaining_stock, dataOfCreation, total_amount))

        conn.commit()
        conn.close()

        return sell_id

    except Exception as e:
        raise ValueError("User creation failed: " + str(e))
    