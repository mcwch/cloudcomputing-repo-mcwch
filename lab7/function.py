from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        name = query_params.get('name', ['World'])[0]
        current_time = datetime.now().strftime("%H:%M:%S")
        response = {
            'body': f'Hello, {name}! The current time is {current_time}.'
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()