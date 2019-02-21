#!/usr/bin/python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'USERNAME MYSQL', 'PASSWORD MYSQL', 'DATABASE MYSQL');
cur = con.cursor()
try:
	sql = "SELECT * from `user` WHERE `id` = '%s'" % ('1')
	cur.execute(sql)
	user = cur.fetchone()
	print "Nama : %s" %user[1]
except:
	print "Select Data Gagal"
        
if con:    
	con.close()
