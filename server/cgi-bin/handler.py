import sys

from cgi import FieldStorage
from http import cookies
import os
import html
import mysql.connector
from _db import Db

sys.stdout.reconfigure(encoding='utf-8')

print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT")
print("Access-Control-Allow-Headers: Content-Type")
# print("Connection: keep-alive")
# print("Content-Type: application/json;charset=UTF-8")
# print("Transfer-Encoding: chunked")
# print("Content-Encoding: br")
print()
# sys.stdin.reconfigure(encoding='utf-8')


# db = Db("localhost", "root", "", "test_mstor")
# print(db.get_cells())
print("Hello")
# if os.environ.get("REQUEST_METHOD") == "POST":
#   print(db.get_cells())
# else:
#   print(db.get_cells())

