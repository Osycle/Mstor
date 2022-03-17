import sys

from cgi import FieldStorage
from http import cookies
import os
import html
import mysql.connector
from _db import Db
import cgitb
cgitb.enable()

sys.stdout.reconfigure(encoding='utf-8')

print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT")
print("Access-Control-Allow-Headers: Content-Type")
print("Cache-Control: no-cache")
print("Pragma: no-cache")
# print("Connection: keep-alive")
# print("Content-Type: application/json;charset=UTF-8")
print("Content-Type: text/html;charset=UTF-8")
# print("Transfer-Encoding: chunked")
# print("Content-Encoding: br")
print()
# sys.stdin.reconfigure(encoding='utf-8')


db = Db("localhost", "root", "", "test_mstor")
print(db.get_cells())
# if os.environ.get("REQUEST_METHOD") == "POST":
#   print(db.get_cells())
# else:
#   print(db.get_cells())

