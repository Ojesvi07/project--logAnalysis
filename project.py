#!/usr/bin/env python3
import psycopg2
import sys
from datetime import datetime
try:
	conn= psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Unable to connect to database!!!")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)


else:
	c=conn.cursor()
	c.execute("select * from new2 order by count desc limit 3;")
	res=c.fetchall()
	c.execute("select * from output2 order by sum desc;")
	res1=c.fetchall()
	c.execute("select * from result1 where res>1.0;")
	res2=c.fetchall()
	print("Top three articles of all time and their total views are")
	for r in res:
		print ('" '+r[0]+' "'+ " - "+str(r[1])+" views")

	print("\n")
	print("Most popular article authors of all time with total page views")
	for r1 in res1:
		print('" '+r1[0]+' "'+" - "+str(r1[1])+" views")
	print("\n")
	print("Date(s) on which requests lead to errors more than 1%")
	for r2 in res2:
		date=r2[0]
		error=r2[1]
		date=datetime.strftime(date,'%b %d, %Y')
		print(date, "-" ,error ,"%errors")
	conn.close()
