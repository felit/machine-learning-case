# -*- coding:utf8 -*-
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='admin',
    db='bill',
    charset="utf8"
)
cur = conn.cursor()
out_file = open('/home/congsl/tmp/bills.txt', 'w+')
cur.execute("SET NAMES utf8")
for i in range(0, 20):
    print '/home/congsl/tmp/bill.txt/0000%02d_0' % i
    file = open('/home/congsl/tmp/bill.txt/0000%02d_0' % i)
    str = file.readline()
    while (str != ''):
        row = str.split('')
        # out_file.write('\t'.join(str.split('')))
        sql = """
            insert into bills(id,dish_id,dish_name)
            values('%s','%s','%s')
        """ % (row[0], row[4], row[5].decode('utf-8'))
        print sql
        cur.execute(sql)
        str = file.readline()
out_file.flush()
out_file.close()


# cur.execute('create table bills(id varchar(64),dish_id varchar(64),dish_name varchar(64))DEFAULT Charset=utf8')

conn.commit()

