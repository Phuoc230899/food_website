from flask import Blueprint, render_template,session,request
from app.db_access import DataProductAccess

index_module = Blueprint("index_module", __name__)
@index_module.route("/")
@index_module.route("/homepage",methods=['GET','POST'])
def index(): 
    connect_db = DataProductAccess()
    per_page = 6
    product_list = connect_db.get_product(per_page)
    cart = []       
    try:
        for prod in session['cart_list']:
            cart.append(prod)          
    except:
        cart = []
    print(cart)    
    return render_template("Pages/index.html",product_list = product_list,cart=cart,quantity=str(len(cart)))
