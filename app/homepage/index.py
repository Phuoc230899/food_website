from flask import Blueprint, render_template,session,request,redirect,url_for
from app.db_access import DataProductAccess

index_module = Blueprint("index_module", __name__)

global cart_list 
cart_list = []

@index_module.route("/")
@index_module.route("/homepage")
def index():
    connect_db = DataProductAccess()
    per_page = 6
    product_list = connect_db.get_product(per_page)
    # cart = []       
    # try:
    #     for prod in session['cart_list']:
    #         cart.append(prod)         q 
    # except:
    #     cart = []
    # print(cart)
    session['cart_list'] = []
    return render_template("Pages/index.html",product_list = product_list)#,cart=cart,quantity=str(len(cart))
