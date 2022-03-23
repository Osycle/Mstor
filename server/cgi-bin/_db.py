
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
    type_dict = isinstance(arr, dict)
    if type_dict:
      arr = [arr]
    for item in arr:
      if isinstance(item, dict):
        for field in item:
          if isinstance(item[field], datetime.datetime):
            item[field] = item[field].timestamp()
          if isinstance(item[field], list):
            self.date_timestamp(item[field])
    if type_dict:
      return arr[0]
    else:
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

  def remove_cell_synapse(self, id):
    try:
      sql = f"DELETE FROM {self.tn_cells_tags} WHERE cell_id = {id}"
      result = self.cursor.execute(sql)
      self.connection.commit()
      return result
    except:
      print("Error remove_tag")

  def remove_tag(self, id):
    try:
      sql = f"DELETE FROM {self.tn_tags} WHERE id = {id}"
      result = self.cursor.execute(sql)
      self.connection.commit()
      return result
    except:
      print("Error remove_tag")

  def remove_cell(self, id):
    try:
      result = {}
      # Выборка единичных тегов этого id в таблице связях
      sql = f"""
        SELECT * FROM {self.tn_cells_tags} 
        WHERE tag_id NOT IN
          (SELECT tag_id FROM {self.tn_cells_tags} 
            WHERE tag_id IN 
              (SELECT tag_id FROM {self.tn_cells_tags} WHERE cell_id IN ({id}))
            AND cell_id NOT IN ({id}))
        AND cell_id IN ({id})  
      """
      self.cursor.execute(sql)
      items = self.cursor.fetchall()
      result["remove_tags"] = 0
      for item in items:
        result["remove_tags"] += self.remove_tag(item["tag_id"]) # Удаление еденичного тега это id
      result["remove_cell_synapse"] = self.remove_cell_synapse(id) # Удаление связи к тегам

      # Удаление ячейки
      sql = f"DELETE FROM {self.tn_cells} WHERE id = {id}"
      result["remove_cell"] = self.cursor.execute(sql)
      self.connection.commit()

      return result
    except:
      print("Error remove_cell")
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
          self.synapse_cell_tag(cell_id, tag["id"])
      return self.give_cell(cell_id)
    finally:
      self.connection.close()

  def edit_cell(self, content):
    print(content)