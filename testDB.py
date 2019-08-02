

import pymysql

# Open database connection
db = pymysql.connect("127.0.0.1","messenger","12345678","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql1="insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) values ('Suraj','Bhosale',24,'female',33000);"
sql2="insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) values ('Sagar','Girhe',24,'female',33000);"
sql3="select * from EMPLOYEE;"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)

results=cursor.fetchall()

for result in results:
    print(result)


# disconnect from server
db.close()
