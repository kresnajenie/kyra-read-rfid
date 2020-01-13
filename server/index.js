// var express = require('express');
// var socket = require('socket.io');
// var app = express();

// var server = app.listen(4000, function() {
//     console.log('listening to requests on port 4000')
// });

// // Static files
// app.use(express.static('public'));

// // Socket Setup
// var io = socket(server);

// io.on('connection', function(socket){
//     console.log('made socket connection', socket.id);

//     socket.on('rfid', function(data) {
//         console.log("data")
//         io.sockets.emit('rfid', data);
//     });
// });

var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(4000);
// WARNING: app.listen(80) will NOT work here!

app.get('/', function (req, res) {
  res.sendFile('C:/Users/Jeremy/programming/kyra-read-rfid/server/public/index.html');
});

io.on('connection', function (socket) {
	console.log("connected", socket.id)

	//Emit Message
  // socket.emit('rfid', { hello: 'world' });
	
	// Listen Message
	socket.on('rfid', function (data) {
    console.log(data);
  });
});