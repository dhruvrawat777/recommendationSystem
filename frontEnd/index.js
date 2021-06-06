var request = new XMLHttpRequest()

function solve2() {
    var s = document.getElementById('movie').value;
    let url = 'http://127.0.0.1:3000/collaborativeBased?id=' + s;
    request.open('GET', url, true);
    request.onload = function () {
        var data = this.response;
        console.log(data);
        document.getElementById('disp').innerHTML =data;
    }
    request.send()
}

function solve() {
    var s = document.getElementById('movie').value;
    console.log(s);
    if (document.getElementById('rec2').checked) {
        solve2();
    }
    else {
        let url = 'http://127.0.0.1:3000/contentBased?id=' + s;
        request.open('GET', url, true);
        request.onload = function () {
            var data = this.response;
            var x = data.split(',');
            document.getElementById('disp').innerHTML = "";
            for (var i = 1; i < x.length - 1; i++) {
                document.getElementById('disp').innerHTML += x[i] + "<br/><br/>";
            }

            //  document.getElementById('disp').innerHTML=data;

        }
        request.send()
    }
}