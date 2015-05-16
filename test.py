# -*- coding: utf-8 -*-
import MySQLdb

connection = MySQLdb.connect(db="test", user="takayuki",passwd="taka3211",host="localhost")
c = connection.cursor()
c.execute("insert into personal (id,name) values(6,'takayuki2')")
#c.execute("select * from name")
#c.execute("delete from personal where name = 'takayuki'")


connection.commit()
c.close()
connection.close()