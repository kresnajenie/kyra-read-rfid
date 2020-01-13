import socketio

def emit_rfid(rfid):
    sio = socketio.Client()

    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def my_message(data):
        # Emit Message
        # rfid is the channel
        sio.emit('rfid', {'rfid': rfid})

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://localhost:4000')
    sio.wait()