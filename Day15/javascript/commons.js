function show_next(id) {
    var div=document.getElementById(id);
    div.classList.remove('hidden');
    var div_father=div.parentNode;
    div_father.classList.add('top_show');
}
function hidden_next(id) {
    var div=document.getElementById(id);
    div.classList.add('hidden');
    var div_father=div.parentNode;
    div_father.classList.remove('top_show');
}
function over_menu_level2(id) {
    var div=document.getElementById(id);
    div.classList.remove('hidden');
}
function out_menu_level2(id) {
    var div=document.getElementById(id);
    div.classList.add('hidden');
}
function show_search_hot() {
    var hot_list=document.getElementsByClassName("search_hot_");
    var search_box=document.getElementById("search_box_");
    for(var i=1;i<hot_list.length;i++){
        if(search_box.value == hot_list[i].innerText){
            break;
        }
    }
    if(i+1<hot_list.length){
        search_box.value=hot_list[i+1].innerText;
    }else{
        search_box.value=hot_list[1].innerText;
    }
}
function show_search_hot_off() {
    clearInterval(time1);
    var search_box=document.getElementById("search_box_");
    search_box.classList.remove("search_box_show");
    search_box.classList.add("search_box_");
    search_box.value=null;
}
function show_poster() {
    var poster_list=document.getElementById("poster_top").children;
    var show_list=document.getElementById("poster_top_show_bar").children;
    for(var i=0;i<8;i++){
        if(poster_list[i].children[0].classList.contains("z-index_1")){
            break;
        }
    }
    if(i+1<8){
        poster_list[i+1].children[0].classList.add("z-index_1");
        show_list[i+1].classList.add("bc-red");
        poster_list[i].children[0].classList.remove("z-index_1");
        show_list[i].classList.remove("bc-red");

    }else {
        poster_list[0].children[0].classList.add("z-index_1");
        show_list[0].classList.add("bc-red");
        poster_list[i].children[0].classList.remove("z-index_1");
        show_list[i].classList.remove("bc-red");
    }
}
function poster_select(id) {
    var poster_list=document.getElementById("poster_top").children;
    var show_list=document.getElementById("poster_top_show_bar").children;
    for(var i=0;i<8;i++){
        if(poster_list[i].children[0].classList.contains("z-index_1")){
            poster_list[i].children[0].classList.remove("z-index_1");
            show_list[i].classList.remove("bc-red");
            break;
        }
    }
    poster_list[id].children[0].classList.add("z-index_1");
    show_list[id].classList.add("bc-red");
}
function show_news_line_left() {
    var news_line=document.getElementById("news_line");
    news_line.classList.remove("news_line_right");
    news_line.classList.add("news_line_left");
    var promotion=document.getElementById("promotion_");
    var notice=document.getElementById("notice_");
    promotion.classList.remove("z-index_1");
    notice.classList.remove("z-index_1");
    promotion.classList.add("z-index_1");
}
function show_news_line_right() {
    var news_line=document.getElementById("news_line");
    news_line.classList.remove("news_line_left");
    news_line.classList.add("news_line_right");
    var promotion=document.getElementById("promotion_");
    var notice=document.getElementById("notice_");
    promotion.classList.remove("z-index_1");
    notice.classList.remove("z-index_1");
    notice.classList.add("z-index_1");
}
function service_select(id) {
    var body_list=document.getElementById("service_body").children;
    var select=document.getElementById("service_select");
    var list=select.classList;
    for(var i=0;i<list.length;i++){
        select.classList.remove(list[i]);
    }
    if(id==2){
        select.classList.add("service_select_plane");
    }else if(id==3){
        select.classList.add("service_select_hotel");
    }else if(id==4){
        select.classList.add("service_select_train");
    }
    for(var j=0;j<body_list.length;j++){
        body_list[j].classList.remove("z-index_1");
    }
    body_list[id-1].classList.add("z-index_1");
}
function sec_kill() {
    var hour_div=document.getElementById("hour");
    var min_div=document.getElementById("minute");
    var sec_div=document.getElementById("second");
    var hour=parseInt(hour_div.innerText);
    var min=parseInt(min_div.innerText);
    var sec=parseInt(sec_div.innerText);
    var time_new=hour*60*60+min*60+sec-1;
    hour=parseInt(time_new/3600);
    min=parseInt((time_new-hour*3600)/60);
    sec=time_new-hour*3600-min*60;
    if(hour<10){
        hour_div.innerText="0"+String(hour)
    }else {
        hour_div.innerText=hour;
    }
    if(min<10){
        min_div.innerText="0"+String(min)
    }else {
        min_div.innerText=min;
    }
    if(sec<10){
        sec_div.innerText="0"+String(sec)
    }else {
        sec_div.innerText=sec;
    }
}
function kill_image_up(id) {
    var image=document.getElementById("kill_body").children[id].children[0].children[0].children[0];
    image.classList.add("kill_product_image_top_up");
    var text=document.getElementById("kill_body").children[id].children[0].children[0].children[2];
    text.classList.add("text_color")
}
function kill_image_down(id) {
    var image=document.getElementById("kill_body").children[id].children[0].children[0].children[0];
    image.classList.remove("kill_product_image_top_up");
    var text=document.getElementById("kill_body").children[id].children[0].children[0].children[2];
    text.classList.remove("text_color")
}
function show_ad() {
    var ad=document.getElementById("ad").children;
    var ad_show=document.getElementById("ad_show_bar").children;
    for(var i=0;i<2;i++){
        if(ad[i].children[0].classList.contains("z-index_1")){
            break;
        }
    }
    if(i+1<2){
        ad[i].children[0].classList.remove("z-index_1");
        ad_show[i].classList.remove("bc-red");
        ad[i+1].children[0].classList.add("z-index_1");
        ad_show[i+1].classList.add("bc-red");
    }else{
        ad[i].children[0].classList.remove("z-index_1");
        ad_show[i].classList.remove("bc-red");
        ad[0].children[0].classList.add("z-index_1");
        ad_show[0].classList.add("bc-red");
    }
}
function ad_select(id) {
    var ad=document.getElementById("ad").children;
    var ad_show=document.getElementById("ad_show_bar").children;
    for(var i=0;i<2;i++){
        if(ad[i].children[0].classList.contains("z-index_1")){
            ad[i].children[0].classList.remove("z-index_1");
            ad_show[i].classList.remove("bc-red");
            break;
        }
    }
    ad[id].children[0].classList.add("z-index_1");
    ad_show[id].classList.add("bc-red");
}
function stop_poster() {
    clearInterval(time2);
}
function start_poster() {
    time2=setInterval("show_poster();",3000);
}
function stop_ad() {
    clearInterval(time4);
}
function start_ad() {
    time4=setInterval("show_ad();",3000);
}
time1=setInterval("show_search_hot();",5000);
time2=setInterval("show_poster();",3000);
time3=setInterval("sec_kill();",1000);
time4=setInterval("show_ad();",3000);
