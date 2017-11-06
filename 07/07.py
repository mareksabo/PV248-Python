import json
import sqlite3
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer


def search_name(searched_name):
    connection = sqlite3.connect('scorelib.dat')
    cursor = connection.cursor()
    cursor.execute("SELECT person.name, score.name FROM score JOIN score_author JOIN person "
                   "ON score.id = score_author.score AND score_author.composer = person.id "
                   "WHERE person.name LIKE ? ORDER BY person.name", ("%{}%".format(searched_name),))

    scores = {}

    for row in cursor:
        if row[0] not in scores:
            scores[row[0]] = []
        scores[row[0]].append(row[1])

    print(scores)
    result = json.dumps(scores, indent=4)
    return result


class LocalHttpServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET called")
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        parsed_url = urlparse(self.path[1:])
        if parsed_url.path != "result":
            message = "Look at /result"
        else:
            message = "You sent <b>{}<b>".format(parsed_url.query)
            dict = parse_qs(parsed_url.query)
            print(dict['q'][0])
            message = search_name(dict['q'][0])
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, LocalHttpServer)
    print('Running server')
    httpd.serve_forever()


run()
