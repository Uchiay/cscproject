import pymysql

def get_connection():
    mypass = "sasuke123"
    mydatabase="bookmanagementsystem"

    con = pymysql.connect(host="bookmanagementsystem.c9gdd4dr2imu.us-east-1.rds.amazonaws.com",user="root",password=mypass,database=mydatabase)

    return con
    

if __name__ == '__main__':
    get_connection()