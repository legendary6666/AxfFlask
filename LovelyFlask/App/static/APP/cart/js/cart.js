$(function () {
    $(".subShopping").click(function () {
        var $subShopping = $(this);

        var $li = $subShopping.parents("li");

        var cartid = $li.attr("cartid");

            console.log(cartid);

        $.getJSON('/axf/subtocart/', {"cartid": cartid}, function (data) {
            console.log(data);

            if (data['status'] = '200'){
                if(data['goods_num'] == '0'){
                    $li.remove();
                }else{
                   $subShopping.next().html(data['goods_num']);
                }

                $(".total_price").html(data["total_price"]);
            }
        })
    })

    $(".confirm").click(function () {
        var $confirm = $(this);

        var $li = $confirm.parents("li");

        var cartid = $li.attr("cartid");
        console.log(cartid);

        $.getJSON('/axf/changecartstatus/', {'cartid': cartid}, function (data) {
            console.log(data);

            if(data["status"] == '200'){
                if(data["select"]){
                    $confirm.find('span').find('span').html('√');

                    if (data['is_all_select']){
                        $(".all_select").find('span').find('span').html('√')
                    }

                }else{
                    $confirm.find('span').find('span').html('');
                    $(".all_select").find('span').find('span').html('');
                }

                $(".total_price").html(data["total_price"]);
            }

        })

    })

    $(".all_select").click(function () {

    /*
        点击全选的时候操作
        如果全都是选中的，需要将全部变成未选中
        如果有未选中的需要将未选中的变成选中
        each 相当于
        for item in items:
        items 在这里代表   $(".confirm") 列表
    */
    selects = [];
    unselects = [];


    $(".confirm").each(function () {

        var $confirm = $(this);
        if($confirm.find('span').find('span').html().length === 0){

            unselects.push($confirm.parents("li").attr('cartid'));

        }else {
            selects.push($confirm.parents("li").attr('cartid'));
        }
    })
    console.log(unselects);
    console.log(selects);

    if(unselects.length > 0){
    //    将未选中的发给服务器                网络传输不支持传送数组，加#转换成字符串传输
        $.getJSON('/axf/changecartsstatus/', {'carts': unselects.join('#'), 'select': true}, function (data) {
            console.log(data);

            if(data["status"] == '200'){
                $(".confirm > span > span").html('√');
                $(".all_select > span > span").html('√');
                $(".total_price").html(data["total_price"]);
            }

        });

    }else {
        $.getJSON('/axf/changecartsstatus/', {'carts': selects.join('#'), 'select': false}, function (data) {
            console.log(data);

            if(data["status"] == '200'){
                $(".confirm > span > span").html('');
                $(".all_select > span > span").html('');
                $(".total_price").html(data["total_price"]);
            }

        })
    }

    });

    $("#make_order").click(function () {

        // 下单，将所有选中的发给服务器
        var selects = [];

        $(".confirm > span > span").each(function () {
            if($(this).html().length > 0){
                selects.push($(this).parents("li").attr('cartid'))
            }
        });

        console.log(selects);
        if(selects.length == 0){
            alert("请选择商品");

        }else{
            $.getJSON('/axf/makeorder/', {'carts': selects.join('#')}, function (data) {
                console.log(data);

                if (data["status"] == '200'){
                    window.open('/axf/orderdetail/?orderid=' + data['order'], target='_self');
                }
            })
        }
    })


})