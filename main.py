
from flask import Flask, request, jsonify
from db.addOpration import createUser, add_product, order_details, available_order
from db.readOpration import getAllUsers, getSpacificUsers, get_spacific_product, get_all_product, get_all_orders_detail, get_order_details_by_filter, get_available_product
from db.updatesOpratons import update_product_details, update_user_all_details, update_order_details
from db.createTableOpration import createTables

app = Flask(__name__)



# Thia is for creating new user in the database

@app.route('/createUser', methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        pinCode = request.form['pinCode']

        user_id = createUser(Name=name, Password=password, Email=email, Address=address, Phone=phone, PinCode=pinCode)

        return jsonify({'message': user_id,'status': 200}), 200

    except Exception as error:
        return jsonify({'message': str(error), 'status': 400}), 400





# This is for get all users details

@app.route('/getAllUsers', methods = ['GET'])
def getAllUser():

    try:

        return getAllUsers()

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400





# This for get spacific user details

@app.route('/getSpacificUser', methods = ["POST"])
def getSpacificUser():

    try:

        userId = request.form['User_id']
        return getSpacificUsers(userId=str(userId))

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400





# This this for comben route for update user, name, password, adress etc here we can pass single value as multipale value as same time

@app.route('/updateUserAllDetails', methods = ['PATCH'])

def updateUserAllDetails():

    try:

        id = request.form['User_id']
        updateUser={}
        for key, value in request.form.items():
            if key != 'User_id':
                updateUser[key] = value
        update_user_all_details(id, **updateUser)

        return jsonify({'message' : 'User Update Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400



















# This is for add new products in the database

@app.route('/addProduct', methods = ['POST'])
def addProduct():

    try:

        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        stack = request.form['stack']
        certified = request.form['certified']

        add_product(name=name, price=price, category=category, stack=stack, certified=certified)

        return jsonify({'message' : 'Add Product Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400



# This is for avaiable products in the database
@app.route('/avaiableProducts', methods = ['POST'])
def availableProducts():

    try:

        user_id = request.form['user_i d']
        product_id = request.form['product_id']
        price = request.form['price']
        product_name = request.form['product_name']
        category = request.form['category']
        stock = request.form['stock']

        available_order(user_id=user_id, product_id=product_id,price=price, product_name=product_name, category=category, stock=stock)

        return jsonify({'message' : 'Add To Available order Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400
    

#This is GetAvailable Products
@app.route('/getAvailableProducts', methods = ['GET'])
def getAvailableProducts():

    try:

        return get_available_product()

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400


# This is for get all product details


@app.route('/getAllProduct', methods = ['GET'])
def getAllProduct():

    try:

        return get_all_product()

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400



# This is for get spacific product details

@app.route('/getSpacificProduct', methods = ['GET'])
def getPpacificProduct():

    try:

        id = request.form['id']

        return get_spacific_product(id=str(id))

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400




# This this for comben route for update product, name, price, category, stack here we can pass single value as multipale value as same time

@app.route('/updateProduct', methods=['PATCH'])
def update_product():

    try:

        id = request.form['id']
        updates = {}

        for key, value in request.form.items():
            if key != 'id':
                updates[key] = value

        update_product_details(id, **updates)

        return jsonify({'message' : 'Product Update Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400





# This is for add order details

@app.route('/addOrderDetails', methods = ['POST'])
def addOrderDetails():
    try:

        Product_id = request.form['product_id']
        User_id = request.form['user_id']
        User_Name = request.form['user_name']
        User_Address = request.form['user_address']
        Phone_Number = request.form['phone']
        Product_name = request.form['product_name']
        Category = request.form['category']
        Total_amount = request.form['total_amount']
        Quantity = request.form['quantity']
        Status = request.form['status']

        order_details(user_id=User_id, user_Name=User_Name, user_address= User_Address, phone=Phone_Number, product_id=Product_id, product_Name= Product_name, category= Category, status=Status, total_amount=Total_amount, quantity=Quantity)

        return jsonify({'message' : 'Order Created Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400



# This is for get all order details

@app.route('/getAllOrdersDetail', methods = ['GET'])
def getAllOrdersDetail():

    try:
        return get_all_orders_detail()

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400





# This is for update order details

@app.route('/updateOrderDetails', methods = ['PATCH'])

def updateOrderDetails():

    try:

        id = request.form['id']
        updateOrder={}
        for key, value in request.form.items():
            if key != 'id':
                updateOrder[key] = value
        update_order_details(id, **updateOrder)

        return jsonify({'message' : 'Order Update Successfully', 'status' : 200}), 200

    except Exception as error:

        return jsonify({'message' : str(error), 'status' : 400 }),400




# This is for get order details by user_id and isApproved

@app.route('/getOrderDetailsByFilter', methods=['POST'])
def getOrderDetailsByFilter():

    try:
        user_id = request.form['user_id']
        isApproved = request.form['isApproved']

        return get_order_details_by_filter(user_id, isApproved)

    except Exception as error:

        return jsonify({'message': str(error), 'status': 400}), 400




if __name__ == "__main__":
    createTables()
    app.run(debug=True, port=5001)

