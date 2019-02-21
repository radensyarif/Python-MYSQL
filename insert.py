#!/usr/bin/python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'USERNAME MYSQL', 'PASSWORD MYSQL', 'DATABASE MYSQL');
cur = con.cursor()
 
sql = "INSERT INTO `user` (`id`,`nama`) VALUE ('%s', '%s')" % (0, "Marjinal")

try:
	cur.execute(sql)
	con.commit()
	print ("Input Data Berhasil")
	print (cur._last_executed)
except:
   con.rollback()
   print ("Input Data Gagal")
   print (cur._last_executed)
	   
       
if con:    
	con.close()
