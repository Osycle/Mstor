
# -*- coding: utf-8 -*-
# python -m pip install mysql-connector-python
# python -m pip install PyMySQL


import sys
from traceback import print_tb
from unittest import result
import mysql.connector
import json
import datetime
import re
import pymysql
import html

# import MySQLdb




class Db:

  tn_cells = "cells"
  tn_tags = "tags"
  tn_cells_tags = "ids_cells_tags"
  
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
  
  def date_timestamp(self, arr):
    for item in arr:
      for field in item:
        if isinstance(item[field], datetime.datetime):
          item[field] = round(item[field].timestamp())
    return arr

  def fetch_cells(self):
    sql = f"SELECT * FROM {self.tn_cells}"
    try:
      self.cursor.execute(sql)
      cells = self.cursor.fetchall()
      for cell in cells:
        tags = self.give_cell_tags(cell["id"])
        cell["tags"] = tags
      return  cells
    finally:
      self.connection.close()

  def remove_cell(self, id):
    sql = f"DELETE FROM {self.tn_cells} WHERE id = {id}"
    try:
      self.cursor.execute(sql)
      self.connection.commit()
      return self.cursor.rowcount
    finally:
      self.connection.close()

  def match_tag(self, tag):
    tag = html.escape(tag)
    sql = f"SELECT * FROM {self.tn_tags} WHERE name = %s"
    try:
      if(self.cursor.execute(sql, tag)):
        return self.cursor.fetchone()
      else:
        return False
    except:
      print("Error match_tag")

  def add_tag(self, tag):
    tag = html.escape(tag)
    sql = f"INSERT INTO {self.tn_tags} (name) VALUES (%s)"
    try:
      self.cursor.execute(sql, tag)
      self.connection.commit()
      sql = f"SELECT * FROM {self.tn_tags} WHERE id = %s"
      self.cursor.execute(sql, self.cursor.lastrowid)
      return self.cursor.fetchone()
    except:
      print("Error add_tag")
  
  def synapse_cell_tag(self, cell_id, tag_id):
    sql = f"INSERT INTO {self.tn_cells_tags} (cell_id, tag_id) VALUES (%s, %s)"
    val = (cell_id, tag_id)
    try:
      self.cursor.execute(sql, val)
      self.connection.commit()
      return True
    except:
      print("Error synapse")

  def give_cell_tags(self, cell_id):
    try:
      sql = f"""
        SELECT * FROM {self.tn_tags} WHERE id IN 
        (SELECT tag_id FROM {self.tn_cells_tags} WHERE cell_id = {cell_id})
      """
      self.cursor.execute(sql)
      tags = self.cursor.fetchall()
      return tags
    except:
      print("Error give_cell_tags")

  def give_cell(self, id):
    sql = f"SELECT * FROM {self.tn_cells} WHERE id IN ({id})"
    try:
      self.cursor.execute(sql)
      cell = self.cursor.fetchone()
      tags = self.give_cell_tags(id)
      cell["tags"] = tags
      return cell
    except:
      print("Error give_cell")


  def add_cell(self, content):
    # olo = self.give_cells()
    # if olo:
    #   self.date_timestamp(olo)
    #   # print(olo)
    # return
    description = content["description"]
    tags = content["tags"]
    sql = f"INSERT INTO {self.tn_cells} (description) VALUES (%s)"
    try:
      self.cursor.execute(sql, description)
      self.connection.commit()
      cell_id = self.cursor.lastrowid
      if not self.cursor.rowcount:
        return
      if(len(tags)):
        for tag_name in tags:
          tag = self.match_tag(tag_name)
          if not tag:
            tag = self.add_tag(tag_name)
          # print(cell_id, tag["id"])
          self.synapse_cell_tag(cell_id, tag["id"])

      cell = self.give_cell(cell_id)
      print(cell)
            
        
    finally:
      self.connection.close()
