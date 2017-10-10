from conf import config
from core.service import FTPService
import socketserver

def run():
    host = config.HOST
    port = config.PORT

    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((host, port), FTPService)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()