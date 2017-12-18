$(function () {
    $('.menu').click(function () {
        if($(this).next().hasClass('menu_content')){
            $(this).next().toggleClass('hide');
        }
    });
    $('.menu_content p').click(function () {
        var flag=true;
        var text=this.innerText;
        $('.tab_bar').children().each(function () {
            if(this.innerText==text){
                $(this).find('.tab_label').addClass('active');
                $(this).siblings().find('.tab_label').removeClass('active');
                $('.content_box').children("[tg='"+text+"']").removeClass('hide');
                $('.content_box').children("[tg='"+text+"']").siblings().addClass('hide');
                flag=false;
            }
        });
        if(flag){
            var tag="<a><div class=\"tab_label active\">\n" +
            "                    <div class=\"tab_label_left\"><div></div></div>\n" +
            "                    <div class=\"tab_label_content\">"+this.innerText+"</div>\n" +
            "                    <div class=\"tab_label_right\"><div></div></div>\n" +
            "                </div></a>";
            $('.tab_bar').children().find('.tab_label').removeClass('active');
            $('.tab_bar').append(tag);
            var tag_con="<div tg=\""+this.innerText+"\" class=\"content\">\n" +
                "                <p>"+this.innerText+"页面正在建设中...</p>\n" +
                "            </div>"
            $('.content_box').children().addClass('hide');
            $('.content_box').append(tag_con);
        }
    });
    $('.tab_bar').delegate('a','click',function () {
        if(this.innerText=='起始页'){
            $('#welcome').removeClass('hide');
            $('#welcome').siblings().addClass('hide');
        }
        $(this).find('.tab_label').addClass('active');
        $(this).siblings().find('.tab_label').removeClass('active');
        $('.content_box').children("[tg='"+this.innerText+"']").removeClass('hide');
        $('.content_box').children("[tg='"+this.innerText+"']").siblings().addClass('hide');
    });
    $('.tab_bar').delegate('a','dblclick',function () {
        if($(this).find('.tab_label').attr('id')=='first'){
            alert('起始页不能关闭');
        }else {
            var con=confirm("确定关闭该标签页吗？");
            if(con){
                $('.content_box').children("[tg='"+this.innerText+"']").remove();
                $(this).remove();
                $('#first').addClass('active');
                $('#welcome').removeClass('hide');
            }
        }
    });
    $('input[name="check_all"]').click(function () {
        $('.tb1').find(':checkbox').prop('checked',true);
        $('.tb1').find('tbody').children().each(function () {
            edit_in(this);
        });
    });
    $('input[name="cancel"]').click(function () {
        $('.tb1').find(':checkbox').prop('checked',false);
        $('.tb1').find('tbody').children().each(function () {
            edit_out(this);
        });
    });
    $('input[name="reverse"]').click(function () {
        $('.tb1').find(':checkbox').each(function () {
            var f=$(this).prop('checked')?false:true;
            $(this).prop('checked',f);
            if(f){
                edit_in($(this).parent().parent()[0]);
            }else {
                edit_out($(this).parent().parent()[0]);
            }
        });
    });
    $('#edit').click(function () {
        if($(this).hasClass('edit_mode')){
            $('.tb1').find('tbody').children().each(function () {
                edit_out(this);
            });
            $(this).removeClass('edit_mode');
            $(this).text('进入编辑模式');
        }else {
            $(this).addClass('edit_mode');
            $(this).text('退出编辑模式');
            $('.tb1').find('tbody').children().each(function () {
                edit_in(this);
            });
        }
    });
    $('.tb1').find(':checkbox').change(function () {
        if($(this).prop('checked')){
            edit_in($(this).parent().parent()[0]);
        }else{
            edit_out($(this).parent().parent()[0]);
        }
    });
    function edit_in(tr) {
        if($(tr).children().eq(0).attr('editing')=='false'){
            if($('#edit').hasClass('edit_mode')){
                if($(tr).find(':checkbox').prop('checked')){
                    var host=$(tr).children().eq(1).text();
                    var port=$(tr).children().eq(2).text();
                    var state=$(tr).children().eq(3).text();
                    $(tr).children().eq(1).html("<input type='text' name='host' value='"+host+"'/>");
                    $(tr).children().eq(2).html("<input type='text' name='port' value='"+port+"'/>");
                    $(tr).children().eq(3).html("<select> <option value='online'>在线</option> <option value='offline'>下线</option> </select>");
                    if(state=='在线'){
                        $(tr).children().eq(3).children().val("online");
                    }else{
                        $(tr).children().eq(3).children().val("offline");
                    }
                    $(tr).children().eq(0).attr('editing','true');
                }
            }
        }
    }
    function edit_out(tr) {
        if($(tr).children().eq(0).attr('editing')=='true'){
            var host=$(tr).find('input[name="host"]').val();
            var port=$(tr).find('input[name="port"]').val();
            var state=$(tr).find('select').val();
            $(tr).children().eq(1).text(host);
            $(tr).children().eq(2).text(port);
            if(state=='online'){
                $(tr).children().eq(3).text('在线');
            }else{
                $(tr).children().eq(3).text('下线');
            }
            $(tr).children().eq(0).attr('editing','false');
        }
    }
});