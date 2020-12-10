#!/usr/bin/env python
# -*- utf-8 -*-


import sys
import time
import datetime
import pymysql
from dateutil.relativedelta import relativedelta
from traceback import format_exc
import json



def insert_record(uid):
    conn = pymysql.connect(host="10.0.10.26", user="risk_test", passwd="risk@risk", db="yingzhongtong_shebao_details")
    acqr_time = int(time.time())
    tid = 185868185538920550 + acqr_time
    task_status = 'AcqrSucc'
    product_id = 68
    partner_code = 'shebao_skip'
    values = [tid, uid, acqr_time, task_status, product_id, partner_code]
    cur = conn.cursor()
    sql = 'INSERT INTO shebao_task_info (`tid`, `uid`, `acqr_time`, `task_status`, `product_id`,  `partner_code`) VALUES (%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, values)
    conn.commit()
    acqr_status = 0
    now = datetime.datetime.now()
    acqr_year_list = [now - relativedelta(years=i) for i in range(3)]
    acqr_year = [dt.year for dt in acqr_year_list]
    for year in acqr_year:
        sql = 'INSERT INTO shebao_acqr_status (`tid`, `acqr_year`, `acqr_status`) VALUES (%s,%s,%s)'
        values = [tid, str(year), acqr_status]
        cur.execute(sql, values)
        conn.commit()



if __name__ == '__main__':
    uid = str(sys.argv[1])
    insert_record(uid)


