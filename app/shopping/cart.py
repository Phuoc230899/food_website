from flask import Blueprint, render_template,request,redirect,url_for,session
from app.db_access import DataProductAccess
import datetime
from datetime import date
import random
import string

cart_module = Blueprint("cart_module", __name__)
global cart_list 
cart_list = [] 

@cart_module.route("/addcart/<string:product_name>")
def addcart(product_name):
    try:   
        user_id = session['user_id'][0]
    except:
        return redirect(url_for('user_module.login'))
    connect_db = DataProductAccess()
    single_product = connect_db.get_singleproduct(product_name)
    price = single_product[2]
    image_path = single_product[5]
    cl = {"product_name": product_name,"price":price,"image_path":image_path}
    cart_list.append(cl)
    session['cart_list'] = cart_list
    return redirect(url_for("index_module.index"))
    
@cart_module.route("/shoppingcart")
def cart():
    connect_db = DataProductAccess()
    cart = []       
    try:
        for prod in session['cart_list']:
            cart.append(prod)          
    except:
        cart = []
    return render_template("pages/shoppingcart.html",cart=cart,quantity=str(len(cart)))

@cart_module.route("/delete/<string:product_name>")
def remove_product(product_name):
    connect_db = DataProductAccess()
    single_product = connect_db.get_singleproduct(product_name)
    price = single_product[2]
    image_path = single_product[5]
    cl = {"product_name": product_name,"price":price,"image_path":image_path}
    cart_list.remove(cl)
    session["cart_list"] = cart_list
    return redirect(url_for("cart_module.cart"))

@cart_module.route("/checkout1",methods=['GET','POST'])
def checkout1():
    connect_db = DataProductAccess()
    cart = []       
    try:
        for prod in session['cart_list']:
            cart.append(prod)          
    except:
        cart = []
    if request.method == 'POST':
        today = date.today()
        email = request.form['email']
        fullname = request.form['fullname']
        address = request.form['address']
        phone = request.form['phone']
        order_date = today.strftime("%b-%d-%Y")
        delivery_date= (datetime.datetime.strptime(order_date, "%b-%d-%Y")+datetime.timedelta(days=4)).strftime("%b-%d-%Y")
        order_number = ''.join(random.choice(string.ascii_uppercase+ string.digits) for _ in range(9))
        return render_template("pages/thankyou.html",email=email,fullname=fullname,address=address,phone=phone,order_date=order_date,delivery_date=delivery_date,order_number=order_number)
    return render_template("pages/checkout1.html",cart=cart,quantity=str(len(cart)))

@cart_module.route("/checkout2")
def checkout2():
    return render_template("pages/checkout2.html")

@cart_module.route("/checkout3")
def checkout3():
    return render_template("pages/checkout3.html")

@cart_module.route("/thankyou")
def thankyou():
    return render_template("pages/thankyou.html")