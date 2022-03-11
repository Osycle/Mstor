import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

from cgi import FieldStorage
from http import cookies
import os
import html


print("Content-Type: text/plain; charset=utf-8")
print("Allow: CONVERT")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type, Authorization, Access-Control-Allow-Methods, Access-Control-Request-Headers")
print()
if os.environ.get("REQUEST_METHOD") == "POST":
  print("OK")
print("Loaded")