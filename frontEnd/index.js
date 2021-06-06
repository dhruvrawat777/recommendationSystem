var request = new XMLHttpRequest()

function solve() {
    var s = document.getElementById('movie').value;
    console.log(s);
    let url='http://127.0.0.1:3000?id='+s;
    request.open('GET',url,true);
    request.onload = function () {
        var data = this.response;
       document.getElementById('disp').innerHTML=data;

    }
    request.send()
}
