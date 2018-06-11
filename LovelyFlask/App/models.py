import hashlib

# Create your models here.
from LovelyFlask.App.ext import db


class Home(db.Model):
    __abstract__ = True
    img = db.Column(db.String(200))
    name = db.Column(db.String(16))
    trackid = db.Column(db.String(64))




class HomeWheel(Home):


    _table__ = 'axf_wheel'

class HomeNav(Home):
    _table__ = 'axf_nav'

class HomeMustBuy(Home):
    _table__ = 'axf_mustbuy'

class HomeShop(Home):
    _table__ = 'axf_shop'

"""
(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,
price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,
img3,childcid3,productid3,longname3,price3,marketprice3)
"""

class HomeMainShow(Home):
    categoryid = db.Column(db.Integer,default=1)

    brandname = db.Column(db.String(32))

    img1 = db.Column(db.String(200))

    childcid1 = db.Column(db.Integer,default=1)

    productid1 = db.Column(db.Integer,default=1)

    longname1 = db.Column(db.String(200))

    price1 =  db.Column(db.Float,default=0)

    marketprice1 = db.Column(db.Float,default=0)

    img2 = db.Column(db.String(200))
    childcid2 = db.Column(db.Integer,default=1)

    productid2 = db.Column(db.Integer,default=1)

    longname2 = db.Column(db.String(200))

    price2 =  db.Column(db.Float,default=0)

    marketprice2 =  db.Column(db.Float,default=0)

    img3 = db.Column(db.String(200))
    childcid3 = db.Column(db.Integer,default=1)

    productid3 = db.Column(db.Integer,default=1)

    longname3 = db.Column(db.String(200))

    price3 =  db.Column(db.Float,default=0)

    marketprice3 =  db.Column(db.Float,default=0)

    _table__ = 'axf_mainshow'

# typeid,typename,childtypenames,typesort

class FoodTypes(db.Model):
    typeid = db.Column(db.Integer,default=1)
    typename = db.Column(db.String(16))
    childtypenames = db.Column(db.String(200))
    typesort = db.Column(db.Integer,default=1)

    _table_ = 'axf_foodtypes'

"""
(productid,productimg,productname,productlongname,isxf,pmdesc,
specifics,price,marketprice,categoryid,childcid,childcidname,
dealerid,storenums,productnum)
("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q",
"","乐吧薯片鲜虾味50.0g",
0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);
"""

class Goods(db.Model):
    productid = db.Column(db.Integer,default=1)
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(200))
    productlongname = db.Column(db.String(200))
    isxf = db.Column(db.Boolean,default=False)
    pmdesc = db.Column(db.Boolean,default=False)
    specifics = db.Column(db.String(200))
    price = db.Column(db.Float,default=0)
    marketprice = db.Column(db.Integer,default=1)
    categoryid = db.Column(db.Integer,default=1)
    childcid = db.Column(db.Integer,default=1)
    childcidname = db.Column(db.String(128))
    dealerid = db.Column(db.Integer,default=1)
    storenums = db.Column(db.Integer,default=1)
    productnum = db.Column(db.Integer,default=1)

    _table_ = 'axf_goods'


class UserModel(db.Model):
    u_name = db.Column(db.String(200),unique=True)
    #

    password = db.Column(db.String(200))
    u_email = db.Column(db.String(32),unique=True)
    u_icon = db.ImageField(upload_to='icons')#******************************
    is_delete = db.Column(db.Boolean,default=False)
    is_active = db.Column(db.Boolean,default=False)

    def generate_hash(self, u_password):
        sha = hashlib.sha512()
        sha.update(u_password.encode("utf-8"))
        return sha.hexdigest()

    def set_password(self, u_password):

        self.password = self.generate_hash(u_password)

    def check_password(self, u_password):
        return self.password == self.generate_hash(u_password)

    _table_ = 'axf_usermodel'

class CartModel(db.Model):
    c_user = db.Column(db.String(32),db.ForeignKey(UserModel))
    c_goods = db.Column(db.String(32),db.ForeignKey(Goods))
    c_goods_num = db.Column(db.Integer,default=1)
    c_goods_select = db.Column(db.Boolean,default=True)

    _table_ = 'axf_cartmodel'

class OrderModel(db.Model):

    o_user = db.Column(db.String(32),db.ForeignKey(UserModel))

    """
        0 已下单，未付款
        1 已下单，已付款，未发货
        2 已下单，已付款，已发货，未收货
    """
    o_status = db.Column(db.Integer,default=0)

    o_time = db.Column(db.DateTime)

    _table_ = 'axf_ordermodel'


class OrderGoods(db.Model):

    o_order = db.Column(db.Integer,db.ForeignKey(OrderModel))

    o_goods = db.Column(db.String,db.ForeignKey(Goods))

    o_goods_num = db.Column(db.Integer,default=1)

    _table_ = 'axf_ordergoods'
