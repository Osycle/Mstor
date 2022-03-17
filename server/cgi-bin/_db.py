
import sys
import mysql.connector
import json
import datetime







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
    self.db = mysql.connector.connect(**self.config)
    self.mycursor = self.db.cursor()
    
  def get_cells(self, sql = ""):
    
    sql = f"SELECT date_time FROM {self.tn_cells}"
    self.mycursor.execute(sql)
    result = self.mycursor.fetchall()
    si = []
    # test = [("sddas1", "sd222dsad"),("zzzzzz1", "xxxxx2")]
    # for line in result:
    #   line = json.dumps(line)
    #   si.append(line)
    for line in result:
      
      si.append(line)
    return si
    # return result[1].timestamp()
    # # mycursor = self.db.cursor()
    # sql = f"SELECT * FROM tags {self.tn_tags}"
    # self.mycursor.execute(sql)
    # ol2 = self.mycursor.fetchall()
    # print(ol2)
    
