import sqlite3
import json



# This is for get all users details

def getAllUsers():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")

    users = cursor.fetchall()
    conn.close()


    userJson = []

    for user in users:
        tempUser = {
            "Id": user[0],
            "User_id": user[1],
            "Password": user[2],
            "Level": user[3],
            "Date_of_account_creation": user[4],
            "isApproved": user[5],
            "Name": user[6],
            "Address": user[7],
            "Email": user[8],
            "Phone": user[9],
            "PinCode": user[10],
        }
        userJson.append(tempUser)
    return json.dumps(userJson)




# This for get spacific user details

def getSpacificUsers(userId):

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute( "SELECT * FROM User WHERE User_id=?", (userId,))

    users = cursor.fetchall()
    conn.close()

    userJson =[]

    for user in users:

        tempUser = {
             "Id": user[0],
            "User_id": user[1],
            "Password": user[2],
            "Level": user[3],
            "Date_of_account_creation": user[4],
            "isApproved": user[5],
            "Name": user[6],
            "Address": user[7],
            "Email": user[8],
            "Phone": user[9],
            "PinCode": user[10]
        }

        userJson.append(tempUser)

    return json.dumps(userJson)


#This the GetAllAvailableProducts

def get_available_product():

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM Available_Products ")
    aps= cursor.fetchall()
    conn.close()

    available_products = []

    for availableProducts in aps:

        tempap = {

            "id" : availableProducts[0],
            "user_id" : availableProducts[1],
            "product_id" : availableProducts[2],
            "price" : availableProducts[3],
            "product_name" : availableProducts[4],
            "category" : availableProducts[5],
            "stock" : availableProducts[6]
            
        
        }

        available_products.append(tempap)

    return  json.dumps(available_products)



# This is for get all product details

def get_all_product():

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM Products ")
    aps= cursor.fetchall()
    conn.close()

    allProducts = []

    for allProduct in aps:

        tempap = {

            "id" : allProduct[0],
            "name" : allProduct[1],
            "price" : allProduct[2],
            "category" : allProduct[3],
            "certified" : allProduct[4],
            "stack" : allProduct[5]
            
        
        }

        allProducts.append(tempap)

    return  json.dumps(allProducts)




# This is for get spacific product details

def get_spacific_product(id):

    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM Products WHERE Products_Id=? ",(id,))
    
    products = cursor.fetchall()
    conn.close()  


    productJson = []
    for product in products:

        tempProducts = {

            "id" : product[0],
            "name" : product[1],
            "price" : product[2],
            "category" : product[3],
            "certified" : product[4],
            "stack" : product[5]
        }

        productJson.append(tempProducts)

    return json.dumps(productJson)


# This is for get all orders detail

def get_all_orders_detail ():

    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM Order_Details")
    details = cursor.fetchall()
    cursor.close()
    deatilsList =[]

    for d in details:

        tempDetails ={

            "id" : d[0],
            "user_id" : d[1],
            "user_name" : d[2],
            "user_address" : d[3],
            "phone": d[4],
            "product_id" : d[5],
            "product_name" : d[6],
            "category": d[7],
            "status" : d[8],
            "isApproved" : d[9],
            "quantity" : d[10],
            "date_of_craete_order" : d[11],
            "total_amount" : d[12],
            "product_price" : d[13],
        }

        deatilsList.append(tempDetails)
    return json.dumps(deatilsList)






# This is for get order details by user_id and isApproved

def get_order_details_by_filter(user_id, isApproved):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Order_Details WHERE user_id = ? AND isApproved = ?
    """, (user_id, isApproved))

    orders = cursor.fetchall()
    conn.close()
    ordersDeatilsList =[]

    for d in orders:

        tempOrdersDeatilsList ={

            "id" : d[0],
            "user_id" : d[1],
            "product_id" : d[2],
            "status" : d[3],
            "isApproved" : d[4],
            "quantity" : d[5],
            "date_of_craete_order" : d[6],
            "total_amount" : d[7],
        }

        ordersDeatilsList.append(tempOrdersDeatilsList)
    return json.dumps(ordersDeatilsList)


def get_sell_details():

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute(" SELECT * FROM Sell_History")
    aps= cursor.fetchall()
    conn.close()

    sell = []

    for Sell in aps:

        tempap = {

            "id" : Sell[0],
            "sell_id" : Sell[1],
            "user_id" : Sell[2],
            "user_name" : Sell[3],
            "product_id" : Sell[4],
            "product_name" : Sell[5],
            "category" : Sell[6],
            "quantity" : Sell[7],
            "remaining_stock" : Sell[8],
            "date_of_create_order" : Sell[9],
            "total_amount" : Sell[10],
        
            
        
        }

        sell.append(tempap)

    return  json.dumps(sell)