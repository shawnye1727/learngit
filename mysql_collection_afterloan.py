import mysql.connector

db_collection = mysql.connector.connect(
    host = "10.0.20.65",
    user = "test_rw",
    passwd = "test_rw_123",
    database = "nc_xiaoying"
	)

loan_id = "196004326543753224"

xy_al_loan_base = f"SELECT *,unix_timestamp() FROM `nc_xiaoying`.`xy_al_loan_base` WHERE `loan_id` = '{loan_id}'"

xy_al_loan_overdue = f"SELECT *,unix_timestamp() FROM `nc_xiaoying`.`xy_al_loan_overdue` WHERE `loan_id` = '{loan_id}'"

xy_al_loan_info_log = f"SELECT *,unix_timestamp() FROM `nc_xiaoying`.`xy_al_loan_info_log` WHERE `loan_id` = '{loan_id}'"

xy_al_loan_repay_plans = f"SELECT *,unix_timestamp() FROM `nc_xiaoying`.`xy_al_loan_repay_plans` WHERE `loan_id` = '{loan_id}'"

xy_al_loan_repay_details = f"SELECT *,unix_timestamp() FROM `nc_xiaoying`.`xy_al_loan_repay_details` WHERE `loan_id` = '{loan_id}'"

sql = [xy_al_loan_base, xy_al_loan_overdue, xy_al_loan_info_log, xy_al_loan_repay_plans, xy_al_loan_repay_details]

mycursor = db_collection.cursor()

sql_result = []

try:
	for i in sql:
		mycursor.execute(i)
		myresult = mycursor.fetchall()
		sql_result.append(myresult)
	print(sql_result)
except Exception as e:
    print(e)
finally:
	mycursor.close()
	db_collection.close()


