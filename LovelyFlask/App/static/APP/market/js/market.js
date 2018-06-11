$(function () {
    $("#all_types").click(function () {
        console.log("全部类型");

        $("#all_type_container").show();

        $(this).find("span").find("span").removeClass("glyphicon-menu-down").addClass("glyphicon-menu-up");
    // 点击左边按钮，隐藏右边
        $("#sort_rule_container").hide();
        $("#sort_rule").find("span").find("span").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down");

    })

    // div上点击隐藏
    $("#all_type_container").click(function () {

        // $(this).hide();
        $(this).slideUp();
        // $(this).slideDown();
        $("#all_types").find("span").find("span").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down");

    });
    // *****************************排序规则的下拉和隐藏*****************************
    $("#sort_rule").click(function () {
        console.log("排序规则")

        $("#sort_rule_container").show();

        $(this).find("span").find("span").removeClass("glyphicon-menu-down").addClass("glyphicon-menu-up");

    // 点击右边按钮，隐藏左边
        $("#all_type_container").hide();
        $("#all_types").find("span").find("span").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down");

    })

    // div上点击隐藏
    $("#sort_rule_container").click(function () {

        // $(this).hide();
        $(this).slideUp();
        // $(this).slideDown();
        $("#sort_rule").find("span").find("span").removeClass("glyphicon-menu-up").addClass("glyphicon-menu-down");
    });

    $(".addShopping").click(function () {
        var $addShopping = $(this);
    //    获取值的两种方式，attr和prop
        console.log($addShopping.prop("goodsid"));
        console.log($addShopping.attr("goodsid"));

        var goodsid = $addShopping.attr("goodsid");
    //    添加到购物车
        $.getJSON('/axf/addtocart/', {"goodsid": goodsid}, function (data) {
            console.log(data);

            if(data['status']==='302'){
                window.open('/axf/userlogin/', target='_self');
            }else if(data["status"]==='200'){

                $addShopping.prev().html(data["goods_num"]);
            }
        });
    })

})