#!/usr/bin/python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'USERNAME MYSQL', 'PASSWORD MYSQL', 'DATABASE MYSQL');
cur = con.cursor()
 
sql = "UPDATE user SET nama = '%s' WHERE `id` = '%s'" % ('Supriadi', '2')

try:
	cur.execute(sql)
	con.commit()
	print "Update Data Berhasil"
	print cur._last_executed
except:
   con.rollback()
   print "Update Data Gagal"
   print cur._last_executed
	   
       
if con:    
	con.close()
