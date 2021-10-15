import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import mysql.connector
import datetime

################################################################
tim = datetime.datetime.now()

ss = str(tim.second)  # time
mi = str(tim.minute)  # time
hh = str(tim.hour)  # time
mm = str(tim.month)  # time
dd = str(tim.day)  # time
yy = str(tim.year)  # time
sheetn = str(yy + "/" + mm + "/" + dd + "\n" + hh + ":" + mi)  # time


def database_func(phone_num, x, y):
    try:
        id_list = []
        print(phone_num, x, y)
        # file = ("E:\\rezz\\car tracker\\course\\website\\accounts\\templates\\sim800.xlsx")
        # xl = pd.ExcelFile(file)
        # shns = xl.sheet_names
        # print(shns)
        # df = pd.read_excel(file, sheet_name=shns[0])
        # print(df)
        # df1 = pd.DataFrame(df)
        # df2 = df1.transpose()
        # df3 = df2.columns
        # print(df3.values)
        # for i in df3:
        #     id_list.append(int(i))
        db = mysql.connector.connect(host="127.0.0.1",
                                     user="root",
                                     password="",
                                     port='3306',
                                     # auth_plugin='mysql_native_password',
                                     db='car_tracker_db'
                                     )

        mycursor = db.cursor()
        # create table
        mycursor.execute("CREATE TABLE IF NOT EXISTS car_tracker_db.sim800 (phone_num varchar(50), x VARCHAR(50),"
                         " y VARCHAR (50),tim VARCHAR(75) )")
        # insert into table
        tim = datetime.datetime.now()
        sql = "INSERT INTO car_tracker_db.sim800 (phone_num,x, y,tim) VALUES (%s,%s, %s,%s)"
        values = (phone_num, x, y, tim)
        mycursor.execute(sql, values)
        db.commit()
    except:
        print("some thing was wrong :(")


def query_database_func(phone):
    try:
        print("p:", phone)
        print(type(phone))
        db = mysql.connector.connect(host="127.0.0.1",
                                     user="root",
                                     password="",
                                     port='3306',
                                     # auth_plugin='mysql_native_password',
                                     db='car_tracker_db'
                                     )
        mycursor = db.cursor()
        sql = "SELECT * FROM car_tracker_db.sim800 WHERE phone_num = " + (phone)
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print('res type', type(myresult))
        for x in myresult:
            print(x)
        return myresult
    except:
        print("error occured )':")
