from flask import Blueprint, request, render_template, url_for

from LovelyFlask.App.models import HomeWheel, HomeNav, HomeMustBuy, HomeMainShow, HomeShop, FoodTypes, Goods, CartModel

blue = Blueprint("first_blue", __name__, url_prefix="/api/")

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)



ALL_TYPE = 0

@blue.route("/home/",methods="GET","POST")
def home():


       wheels = HomeWheel.query.all()
       navs = HomeNav.query.all()
       mustbuys = HomeMustBuy.query.all()
       mainshows = HomeMainShow.query.all()

       shops = HomeShop.query.all()

       shops0_1 = shops[0:1]
       shops1_3 = shops[1:3]
       shops3_7 = shops[3:7]
       shops7_11 = shops[7:11]

       data = {
           "wheels": wheels,
           "navs": navs,
           "mustbuys": mustbuys,
           'shops0_1': shops0_1,
           'shops1_3': shops1_3,
           'shops3_7': shops3_7,
           'shops7_11': shops7_11,
           'mainshows': mainshows,
       }

       return render_template("test.html")


def market(request):
    #先给了一个默认值，然后就可以直接跳转到这个页面
    return  render_template(url_for("marketWithParams"))



def marketWithParams(request, categoryid,childcid):
    foods = FoodTypes.objects.all()
    if ALL_TYPE == 0:
        goods_list = Goods.objects.all().filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.all().filter(categoryid = categoryid).filter(childcid=childcid)

    food = FoodTypes.query.get(typeid=categoryid)
    #food 是每一个视频分类对象

    #得到属性childtypenames,然后是一个字符串的形式，而且这个每一个信息中间有#
    childtypestr = food.childtypenames

    #以#分割得到一个列表
    childtypelist = childtypestr.split("#")

    #以遍历 的形式将这个列表，遍历，并将这个列表的每一个元素以：分割，添加到一个控列表中，得到一个
    #嵌套列表
    childlist = []
    for child in childtypelist:
        childlist.append(child.split(":"))
    #[["全部分类，0“]，["进口水果"，110]]
    #将得到的这个列表，元素遍历出来，得到遍历出来的小列表，将小列表索引为0 的元素拿出来当做是页面显示的东西。


    data = {
        "title":"闪购",
        "foods":foods,
        "goods_list":goods_list,
        "categoryid":categoryid,
        "childlist":childlist,
    }

    return render_template('/html/market/market.html',context=data)


def cart(request):

    userid = request.session.get("user_id")

    if not userid:
        return render_template(url_for(""))

    carts = CartModel.objects.filter(c_user_id=userid)

    is_all_select = True

    totalprice = 0

    # 总价应该在一进页面就开始算.应该是选中的都算进去
    for cart in carts:

        if not cart.c_goods_select:

            is_all_select = False
            #break当有未选中的时候等于false然后选中的需要进行计算价格
        else:
            totalprice = totalprice + cart.c_goods_num * cart.c_goods.price

    data = {
        "title":"购物车",
        "carts":carts,
        "is_all_select":is_all_select,
        "totalprice":totalprice
    }

    return render_template('/html/cart/cart.html',context=data)









