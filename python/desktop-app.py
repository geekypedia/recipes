from cefpython3 import cefpython as cef
from bottle import route, run, response, static_file
from json import dumps
import os 
import sys
import threading

host = "127.0.0.1"
port = "8080"
app = "Sample App"
url = "http://{}:{}".format(host, port)
root_folder = os.path.dirname(os.path.realpath(__file__))
entry_file = "index.html"

def jsonify(data):
    response.content_type = 'application/json'
    return dumps(data)

@route('/')
def index():
    global entry_file, root_folder
    return static_file(entry_file, root_folder)


def server():
    global port
    run(port=port) 

def client():
    global host, port, app
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url=url, window_title=app)
    cef.MessageLoop()
    cef.Shutdown()

def main():
    server_thread = threading.Thread(target=server)
    server_thread.start()
    client()
    
main()