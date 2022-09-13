import psycopg2
from app import app


class DataAccountAccess:
    def __init__(self):
        self.cur = None
        self.conn = None

    def connect_db(self):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                host="localhost",
                database="FoodDB",
                user="root",
                password="tpos123",
            )
            # create a cursor
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            print("Unable to connect %s" % str(e))
            return None

    def check_login(self,email,password):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'SELECT * FROM accounts Where email = %s and password = %s ',
                (email, password)
            )
            # display the PostgreSQL database server version
            account_info = self.cur.fetchall()
            if len(account_info) > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Check Login error: "+str(e))
            return False

    def check_register(self,email):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'SELECT * FROM accounts Where email = %s',
                (email,)
            )
            # display the PostgreSQL database server version
            account_info = self.cur.fetchall()
            if len(account_info) > 0:
                return False
            else:
                return True
        except Exception as e:
            print("Check Register error: "+str(e))
            return False

    def create_account(self,username,email,password):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'Insert Into accounts(username,email,password) Values(%s,%s,%s)',
                (username,email,password)
            )
            self.conn.commit()
            self.cur.close()
            return True
        except Exception as e:
            print("Create Account error: "+str(e))
            return False

    def get_user_id(self,email):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'Select user_id from accounts Where email=%s',
                (email,)
            )
            user_id = self.cur.fetchone()
            return user_id
        except Exception as e:
            print("Create Account error: "+str(e))
            return None

class DataProductAccess:
    def __init__(self):
        self.cur = None
        self.conn = None

    def connect_db(self):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                host="localhost",
                database="FoodDB",
                user="root",
                password="tpos123",
            )
            # create a cursor
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            print("Unable to connect %s" % str(e))
            return None

    def get_product(self,limit_product):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select * From products Limit %s',(limit_product,))
            list_product = self.cur.fetchall()
            return list_product
        except Exception as e:
            print("Get Product error: "+str(e))
            return None

    def add_to_cart(self,user_id,product_name,quality,date_order):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Insert Into cart (user_id,product_name,quality,date_order) values(%s,%s,%s,%s)',(user_id,product_name,quality,date_order,))
            self.conn.commit()
            self.cur.close()
            return True
        except Exception as e:
            print("Get Product error: "+str(e))
            return False
    
    def get_singleproduct(self,product_name):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select * From products Where product_name=%s',(product_name,))
            single_product = self.cur.fetchone()
            return single_product
        except Exception as e:
            print("Get Product error: "+str(e))
            return None       