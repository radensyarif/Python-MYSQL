#!/usr/bin/python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'USERNAME MYSQL', 'PASSWORD MYSQL', 'DATABASE MYSQL');
cur = con.cursor()
 
sql = "DELETE FROM `user` WHERE `id` = '%s'" % ("6")

try:
	cur.execute(sql)
	con.commit()
	print "Hapus Data Berhasil"
	print cur._last_executed
except:
   con.rollback()
   print "Hapus Data Gagal"
   print cur._last_executed
	   
       
if con:    
	con.close()
