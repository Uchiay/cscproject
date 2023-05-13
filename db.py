import pymysql

def get_connection():
    mypass = "lancaster123"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)

    return con
    

if __name__ == '__main__':
    get_connection()