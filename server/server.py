
import cgi
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler
CGIHTTPRequestHandler.cgi_directories = ["/cgi-bin", "/gbook"]
PORT = 4444
server_address = ("", PORT)
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
      

# class MyHttpServer(BaseHTTPRequestHandler):
#   def do_GET(self):
#     self.send_response(200)
#     self.send_header("Content-Type", "text/html")
#     self.end_headers()
#     msg = "Hellow"
#     self.wfile.write(msg.encode("utf-8"))


# print(sys.stdout.encoding)

class MyHttp(CGIHTTPRequestHandler):
  def do_OPTIONS(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
    self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")
    self.send_header("Access-Control-Allow-Headers", "Authorization")
    self.send_header("Allow", "CONVERT")
    self.end_headers()
  def do_GET(self):  
    self.send_response(200)
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
    self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Authorization")
    self.end_headers()
    msg = "<h1>Привет</h1>"+self.path
    self.wfile.write(msg.encode("utf-8"))

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)



print("Liste: ", PORT)
httpd.serve_forever()
# -*- coding: utf-8 -*-