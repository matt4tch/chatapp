var socket = io.connect("://" + location.hostname + ":" + location.port);
var x = 5;
let y = 7;
//alert("http://" + location.hostname + ":" + location.port);

function sum(x, y) {
    return x + y;
}