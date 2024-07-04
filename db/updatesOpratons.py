
import sqlite3



# This is for comben fancation for update product, name, price, category, stack here we can pass single value as multipale value as same time

def update_product_details(id, **kwargs):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    for keyes, value in kwargs.items():
        if keyes == 'name':
            cursor.execute("UPDATE Products SET name=? WHERE Products_Id=?", (value, id))
        elif keyes == 'price':
            cursor.execute("UPDATE Products SET price=? WHERE Products_Id=?", (value, id))
        elif keyes == 'category':
            cursor.execute("UPDATE Products SET category=? WHERE Products_Id=?", (value, id))
        elif keyes == 'stack':
            cursor.execute("UPDATE Products SET stack=? WHERE Products_Id=?", (value, id))
        elif keyes == 'certified':
            cursor.execute("UPDATE Products SET certified=? WHERE Products_Id=?", (value, id))

    conn.commit()
    conn.close()






# This this for comben funcation for update user, name, password, adress etc here we can pass single value as multipale value as same time

def update_user_all_details(id, **keyword):

    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    for key, value in keyword.items():

        if key == 'Name':
            cursor.execute(" UPDATE User SET Name=? WHERE User_id=?",(value,id))

        elif key == 'Password':
            cursor.execute(" UPDATE User SET Password=? WHERE User_id=?",(value,id))
        
        elif key == 'Level':
            cursor.execute(" UPDATE User SET Level=? WHERE User_id=?",(value,id))

        elif key == 'Date_of_account_creation':
            cursor.execute("UPDATE User SET Date_of_account_creation=? WHERE User_id=?",(value,id))

        elif key == 'isApproved':
            cursor.execute(" UPDATE User SET isApproved=? WHERE User_id=?",(value,id))

        elif key == 'Address':
            cursor.execute(" UPDATE User SET Address=? WHERE User_id=?", (value, id))

        elif key == 'Email':
            cursor.execute(" UPDATE User SET Email=? WHERE User_id=?", (value,id))

        elif key == 'Phone':
            cursor.execute(" UPDATE User SET Phone=? WHERE User_id=?", (value,id))

        elif key == ' PinCode':
            cursor.execute(" UPDATE User SET PinCode=? WHERE User_id=?",(value,id))

    
    conn.commit()
    conn.close()







# This is for update order details

def update_order_details(id, **keyword):

    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    for key, value in keyword.items():

        if key == 'user_id':
            cursor.execute(" UPDATE Order_Details SET user_id=? WHERE Id=?",(value,id))

        elif key == 'product_id':
            cursor.execute(" UPDATE Order_Details SET product_id=? WHERE Id=?",(value,id))
        
        elif key == 'status':
            cursor.execute(" UPDATE Order_Details SET status=? WHERE Id=?",(value,id))

        elif key == 'isApproved':
            cursor.execute("UPDATE Order_Details SET isApproved=? WHERE Id=?",(value,id))

        elif key == 'quantity':
            cursor.execute(" UPDATE Order_Details SET quantity=? WHERE Id=?",(value,id))

        elif key == 'date_of_craete_order':
            cursor.execute(" UPDATE Order_Details SET date_of_craete_order=? WHERE Id=?", (value,id))

        elif key == 'total_amount':
            cursor.execute(" UPDATE Order_Details SET total_amount=? WHERE Id=?", (value, id))


    conn.commit()
    conn.close()    