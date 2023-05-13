
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = pymysql.connect(host="library.c9gdd4dr2imu.us-east-1.rds.amazonaws.com",user="admin",password="lancaster",database="library", port=3306)
cur = con.cursor()

print(cur)
