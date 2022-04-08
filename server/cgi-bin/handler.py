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
print("Content-Type: text/html;charset=UTF-8")
# print("Transfer-Encoding: chunked")
# print("Content-Encoding: br")
print()




db = Db("localhost", "root", "", "test_mstor")




if os.environ.get("REQUEST_METHOD") == "POST":

  from urllib.parse import parse_qs

  content_len = os.environ.get('CONTENT_LENGTH', '0')
  method = os.environ.get('REQUEST_METHOD', '')
  query_string = os.environ.get('QUERY_STRING', '')

  if query_string:
    print("this query string")
    exit()

  body = sys.stdin.read(int(content_len))

  try:
    result = json.loads(body)
  except:
    print("this is not json")
    exit()

  if "action" in result:
    if(result["action"] == "wiki"):
      import wikipedia
      # wikipedia.search("Митохондрия", results=2) # Ищет заголовки
      wikipedia.set_lang("ru")
      
      # titles = wikipedia.search("Митохондрия", results=2) 
      # suggest = wikipedia.suggest("Гугл") 
      # summary = wikipedia.summary("Митохондрия",  sentences=5) 
      page = wikipedia.page("Митохондрия") 
      print(page.summary)
      
      print("<br>")
      carousel = ""
      # for image in page.images:
        # carousel += f"<img src='{image}'>"
      print(f"<img src='{page.images[0]}'>")
      exit()
    if(result["action"] == "search"):
      query = result["query"]
      found = db.search(query)
      found = db.date_timestamp(found)
      result = {
        "status": True,
        "count": len(found),
        "cells": found
      }
      result = json.dumps(result)
      print(result)
      exit()
    if(result["action"] == "fetch_cells"):
      cells = db.fetch_cells()
      tags = db.give_tags()
      result = {
        "status": True,
        "cells": cells,
        "tags": tags
      }
      result = db.date_timestamp(result)
      result = json.dumps(result)
      print(result)
      db.connection.close()
      exit()
    if(result["action"] == "delete_cell"):
      count = db.remove_cell(result["cell_id"])
      result = {
        "status": True,
        "count": count
      }
      result = json.dumps(result)
      print(result)
      exit()
    if(result["action"] == "add_cell"):
      cell = db.add_cell(result["content"])
      cell = db.date_timestamp(cell)
      result = {
        "status": True,
        "cell": cell
      }
      result = json.dumps(result)
      print(result)
      exit()
    if(result["action"] == "edit_cell"):
      cell = db.edit_cell(result["content"])
      cell = db.date_timestamp(cell)
      result = {
        "status": True,
        "cell": cell
      }
      result = json.dumps(result)
      print(result)
      exit()


    print("'action' Key not found")



  # query = parse_qs(query_string)
  # print('test: ', query['test'][0])



# print(db.fetch_cells())

