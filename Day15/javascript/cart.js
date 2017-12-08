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