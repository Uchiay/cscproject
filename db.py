import pymysql

def get_connection():
    mypass = "Sasuke@123" ###"sasuke123"
    mydatabase='bookmanagementsystem'
    hostname="bookmanagementsystem.c9gdd4dr2imu.us-east-1.rds.amazonaws.com"

    con = pymysql.connect(host="localhost",
                            user="admin",
                            password=mypass,
                            database=mydatabase)

    print(con)
    return con
    

if __name__ == '__main__':
    get_connection()