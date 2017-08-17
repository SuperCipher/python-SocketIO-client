from socketIO_client import SocketIO

def on_bbb_response(*args):
    print 'on_bbb_response', args

with SocketIO('localhost', 3000) as socketIO:
    socketIO.emit('chat message', "hi from python", on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)
