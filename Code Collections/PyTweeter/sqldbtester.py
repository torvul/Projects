# THIS IS THE BEST WAY TO TEST IF IT IS WORKING WELL
# It just prints the connection for the db

import MySQLdb


mydb = MySQLdb.connect(
    host="localhost",
    database='sys',
    user="root",
    password="i95lk20ds2W!"

        )


cur = mydb.cursor()

cur.execute("Select * From TweetCollection")

for row in cur.fetchall():
    print(row[0], " ", row[1] , " " , row[2] , " " , row[3], " " , row[4])




