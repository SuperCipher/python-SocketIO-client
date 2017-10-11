# garantee working
# from socketIO_client import SocketIO
#
# def on_bbb_response(*args):
#     print ('on_bbb_response', args)
#
# with SocketIO('localhost', 8080) as socketIO:
#     socketIO.emit('fps_com', "hi from python", on_bbb_response)
#     socketIO.wait_for_callbacks(seconds=1)

import logging
from socketIO_client import SocketIO, BaseNamespace
# ,LoggingNamespace for more detail

logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()


def on_test_response(*args):
    print('on_test_response', args)


def on_connect():
    print('connect')


def on_disconnect():
    print('disconnect')


def on_fps_com_response(*args):
    print('on_fps_com_response', args)
    print(type(args))
    # print(args['xxx'])
    print(args[0])



class FpsNamespace(BaseNamespace):

    def on_fps_com_response(self, *args):
        print('on_fps_com_response', args)


# ,LoggingNamespace for more detail
socketIO = SocketIO('http://127.0.0.1', 8082, verify=False)
FpsNamespace = socketIO.define(FpsNamespace, '/fps-namespace')

FpsNamespace.emit('fps_com', 'aaa')
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
# socketIO.on_message(data, '/fps-namespace')
# print(data)
FpsNamespace.on('fps_com', on_fps_com_response)

socketIO.wait(seconds=5)


# from socketIO_client import SocketIO, LoggingNamespace
#
# def on_connect():
#     print('connect')
#
#
# def on_disconnect():
#     print('disconnect')
#
# def on_reconnect():
#     print('reconnect')
#
# def on_fps_com_response(*args):
#     print('on_fps_com_response', args)
#
# socketIO = SocketIO('localhost', 8080)
# socketIO.on('connect', on_connect)
# socketIO.on('disconnect', on_disconnect)
# socketIO.on('reconnect', on_reconnect)
#
# # Listen
# socketIO.on('fps_com', on_fps_com_response)
# socketIO.emit('fps_com', 'connecting from python')
# socketIO.wait()


#
# from socketIO_client import SocketIO, LoggingNamespace
#
# def  on_bbb_response(*args):
#     print('on_bbb_response', args)
#
# with SocketIO('localhost', 8080) as socketIO:
#     socketIO.emit('fps_com', {'xxx': 'yyy'}, on_bbb_response)
#     socketIO.wait_for_callbacks(seconds=1)
