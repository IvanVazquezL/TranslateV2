var words = document.querySelectorAll(".tooltips");


var tooltips = document.querySelectorAll('.tooltips span');

window.onmousemove = function (e) {
    var x = (e.clientX + 10) + 'px',
        y = (e.clientY + 20) + 'px',
        yp = (e.clientY - 40) + 'px';


    for (var i = 0; i < tooltips.length; i++) {
      tooltips[i].style.top = y;
      tooltips[i].style.left = x
    }


};
