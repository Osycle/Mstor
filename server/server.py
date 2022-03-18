import cgi
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler
# import socketserver
CGIHTTPRequestHandler.cgi_directories = ["/cgi-bin"]
PORT = 4040
server_address = ("127.0.0.1", PORT)

# print(CGIHTTPRequestHandler.responses)

# class MyHttp(CGIHTTPRequestHandler):
#   def do_GET(self):  
#     self.send_response(200)
#     self.send_header("Content-Type", "text/html; charset=utf-8")
#     self.send_header('Access-Control-Allow-Origin', '*')
#     self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
#     self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Authorization")
#     self.end_headers()
#     msg = "Привет"
#     self.wfile.write(msg.encode("utf-8"))
#   def do_OPTIONS(self):
#     self.send_response(200)
#     self.send_header('Access-Control-Allow-Origin', '*')
#     self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
#     self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Authorization")
#     self.end_headers()

# print(sys.stdout.encoding)

class MyHttp(CGIHTTPRequestHandler):
  def do_OPTIONS(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.end_headers()
  # def do_POST(self):  
  #   self.send_response(200)
  #   self.send_header("Content-Type", "text/html; charset=utf-8")
  #   self.send_header('Access-Control-Allow-Origin', '*')
  #   self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
  #   self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Authorization")
  #   self.end_headers()
  #   msg = "<h1>Привет</h1>"
  #   self.wfile.write(msg.encode("utf-8"))

sys.stdout.reconfigure(encoding='utf-8')

httpd = HTTPServer(server_address, MyHttp)
# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(server_address, CGIHTTPRequestHandler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
print("Listen: ", PORT)
httpd.serve_forever()