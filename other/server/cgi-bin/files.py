import sys

import cgi
import json
from http import cookies
import os
import html
import mysql.connector
from _db import Db

import cgitb
cgitb.enable()

import pymysql
import pymysql.cursors


sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')




print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT")
print("Access-Control-Allow-Headers: Content-Type")
print("Cache-Control: no-cache")
print("Pragma: no-cache")
# print("Connection: keep-alive")
# print("Content-Type: application/json;charset=UTF-8")
print("Content-Type: image/png;charset=UTF-8")
# print("Transfer-Encoding: chunked")
# print("Content-Encoding: br")
print()

# import urllib.request
# url = "https://pp.vk.me/c540104/c624218/v624218602/3321/uYVa4FQv_q0.jpg"
# img = urllib.request.urlopen(url).read()
# out = open("../img.jpg", "wb")
# out.write(img)
# out.close


db = Db("localhost", "root", "", "test_mstor")

params = cgi.FieldStorage()
img = params.getvalue("image")
print(img)