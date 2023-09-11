// function to display a message on the client-side
async function add_messages(msg, scroll) {
    if (typeof msg.name !== "undefined") {
      var date = dateNow();
  
      if (typeof msg.time !== "undefined") {
        var n = msg.time;
      } else {
        var n = date;
      }
      var global_name = await load_name();
  
      var content;
      if (global_name == msg.name) {
        content =
            '<div class="container darker">' +
            '<b style="color:#000" class="left">' +
            msg.name +
            "</b><p>" +
            msg.message +
            '</p><span class="time-left">' +
            n +
            "</span></div>";
      } else {
        content = '<div class="container">' +
            '<b style="color:#000" class="right">' +
            msg.name +
            "</b><p>" +
            msg.message +
            '</p><span class="time-right">' +
            n +
            "</span></div>";
      }
      // update div
      var messageDiv = document.getElementById("messages");
      messageDiv.innerHTML += content;
    }
  
    if (scroll) {
      scrollSmoothToBottom("messages");
    }
}

// Fetch API request to fetch user's name from server & pass it to the front-end
async function load_name() {
    return await fetch("/get_name")
      .then(async function (response) {
        return await response.json();
      })
      .then(function (text) {
        return text["name"];
      });   
}

// Establish a socketio connection
var socket = io.connect("http://" + location.hostname + ":" + location.port);
socket.on("connect", async function () {
  var usr_name = await load_name();
  if (usr_name != "") {
    socket.emit("event", {
      message: usr_name + " just connected to the server!",
      connect: true,
    });
  }
  var form = $("form#msgForm").on("submit", async function (e) {
    e.preventDefault();

    // get input from message box
    let msg_input = document.getElementById("msg");
    let user_input = msg_input.value;
    let user_name = await load_name();
    console.log(user_input);

    // clear msg box value
    msg_input.value = "";

    // send message to the server, so that it can be sent to all users via SocketIO
    socket.emit("event", {
        name: user_name,
        message: user_input,
    });
  });
});

socket.on("disconnect", async function (msg) { 
  var usr_name = await load_name();
  socket.emit("event", {
    message: usr_name + " just left the server...",
  });
});

// Event listener for a message sent by the server
socket.on("message response", function (msg) {
  add_messages(msg, true);
});

function scrollSmoothToBottom(id) {
    var div = document.getElementById(id);
    // Boilerplate JQuery to perform an animated scroll operation
    $("#" + id).animate(
      {
        scrollTop: div.scrollHeight - div.clientHeight,
      },
      500
    );
  }

function dateNow() {
    var date = new Date();
    var aaaa = date.getFullYear();
    var gg = date.getDate().toString().padStart(2, '0');
    var mm = (date.getMonth() + 1).toString().padStart(2, '0');
  
    var cur_day = aaaa + "-" + mm + "-" + gg;
  
    var hours = date.getHours().toString().padStart(2, '0');
    var minutes = date.getMinutes().toString().padStart(2, '0');
    var seconds = date.getSeconds().toString().padStart(2, '0');
  
    return cur_day + " " + hours + ":" + minutes + ":" + seconds;
}