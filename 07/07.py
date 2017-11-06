import json
import sqlite3
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

from json2html import *


def search_name(searched_name, is_json):
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
    json_output = json.dumps(scores, indent=4)
    if is_json:
        return json_output
    else:
        return json2html.convert(json=json_output)


class LocalHttpServer(BaseHTTPRequestHandler):
    def do_GET(self):
        is_json = False
        parsed_url = urlparse(self.path[1:])
        if parsed_url.path != "result":
            message = "Look at /result"
        else:
            d = parse_qs(parsed_url.query)
            is_json = 'json' == d['f'][0] if ('f' in d) else False
            searched_name = d['q'][0] if ('q' in d) else ""
            message = search_name(searched_name, is_json)

        self.send_response(200, 'OK')
        format_type = 'json' if is_json else 'html'
        self.send_header('Content-type', 'text/' + format_type + '; charset=utf-8')
        self.end_headers()

        self.wfile.write(message.encode())
        return


def run():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, LocalHttpServer)
    print('Running server')
    httpd.serve_forever()


run()
