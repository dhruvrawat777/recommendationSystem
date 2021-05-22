var request = new XMLHttpRequest()

request.open('GET', 'http://localhost:3000/search', true)

request.onload = function () {
    var data = JSON.parse(this.response)
    console.log(data)
    data.forEach((x) => {
        document.getElementById('disp').innerHTML += x;
    })

}

request.send()
