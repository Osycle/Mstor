
# -*- coding: utf-8 -*-
# python -m pip install mysql-connector-python
# python -m pip install PyMySQL


import sys
import mysql.connector
import json
import datetime
import re
import pymysql
import pymysql.cursors





class Db:

  tn_cells = "cells"
  tn_tags = "tags"
  tn_ids_cells_tags = "ids_cells_tag"
  
  def __init__(self, host, user, password, database):

    self.config = {
      "host": host,
      "user": user,
      "password": password,
      "database": database
    }
    self.connection = pymysql.connect(
      host=host, 
      user=user, 
      password=password, 
      database=database,
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor)
    self.cursor = self.connection.cursor()
    
  def get_cells(self, sql = ""):
    sql = f"SELECT * FROM {self.tn_cells}"
    try:
      self.cursor.execute("SELECT * FROM cells")
      rows = self.cursor.fetchall()
      cells = []
      for row in rows:
        row["date_time"] = round(row["date_time"].timestamp())
        row["date_time_edit"] = round(row["date_time_edit"].timestamp())
        cells.append(row)

      result = {
        "cells": cells
      }
      return json.dumps(result)
    finally:
      self.connection.close()

