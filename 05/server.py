import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer


class LocalHttpServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET called")
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "You sent <b>{}<b>".format(self.path[1:])
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, LocalHttpServer)
    print('Running server')
    httpd.serve_forever()


run()
