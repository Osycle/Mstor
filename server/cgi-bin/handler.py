import sys

from cgi import FieldStorage
from http import cookies
import os
import html
import mysql.connector
from _db import Db


print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type, Authorization, Access-Control-Allow-Methods, Access-Control-Request-Headers")
# print("Content-Type: application/json; charset=utf-8")
print()
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

db = Db("localhost", "root", "", "test_mstor")
if os.environ.get("REQUEST_METHOD") == "POST":
  print(db.get_cells())
else:
  print(db.get_cells())

