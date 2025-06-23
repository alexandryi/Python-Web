import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import socket
from datetime import datetime

HOST = 'localhost'
HTTP_PORT = 3000
SOCKET_PORT = 5000
DATA_FILE = 'storage/data.json'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FRONT_DIR = os.path.join(BASE_DIR, 'front') 

os.makedirs('storage', exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/' or path == '/index.html':
            self.send_html_file('index.html')
        elif path == '/message.html':
            self.send_html_file('message.html')
        elif path.startswith('/style.css'):
            self.send_static_file('style.css', 'text/css')
        elif path.startswith('/logo.png'):
            self.send_static_file('logo.png', 'image/png')
        else:
            self.send_html_file('error.html', code=404)

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(post_data, (HOST, SOCKET_PORT))
            sock.close()
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_html_file('error.html', code=404)

    def send_html_file(self, filename, code=200):
        file_path = os.path.join('front', filename)
        try:
            with open(file_path, 'rb') as f:
                self.send_response(code)
                if filename.endswith('.html'):
                    self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def send_static_file(self, filename, content_type):
        file_path = os.path.join('front', filename)
        try:
            with open(file_path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')


def run_http_server():
    server_address = (HOST, HTTP_PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"HTTP Server running at http://{HOST}:{HTTP_PORT}")
    httpd.serve_forever()


def run_socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, SOCKET_PORT))
    print(f"Socket Server running at {HOST}:{SOCKET_PORT}")

    while True:
        data, addr = sock.recvfrom(1024)
        parsed_data = parse_qs(data.decode())
        username = parsed_data.get('username', [''])[0]
        message = parsed_data.get('message', [''])[0]

        if username and message:
            timestamp = str(datetime.now())
            record = {timestamp: {'username': username, 'message': message}}

            with open(DATA_FILE, 'r') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = {}

            existing_data.update(record)
            with open(DATA_FILE, 'w') as f:
                json.dump(existing_data, f, indent=4)


if __name__ == '__main__':
    http_thread = threading.Thread(target=run_http_server)
    socket_thread = threading.Thread(target=run_socket_server)

    http_thread.start()
    socket_thread.start()

    http_thread.join()
    socket_thread.join()
