import sqlite3


# cursor.execute("DROP TABLE tbl_users")
# cursor.execute("CREATE TABLE tbl_users(uname VARCHAR(500) PRIMARY KEY,user_level VARCHAR(20) DEFAULT 'cashier',  passw VARCHAR(500));")
# cursor.execute("INSERT INTO tbl_users VALUES('Calvine22','admin','1234')")
# cursor.execute("INSERT INTO tbl_users VALUES('Calvine2','admin','1234')")
# cursor.execute("INSERT INTO tbl_users VALUES('Calvine','cashier','1234')")
# db.commit()

def try_login(username,level,password):
    try:
        db=sqlite3.connect('./database/PHotel.db',check_same_thread=False)
        cursor=db.cursor()
    except:
        return "Error Connectig to database"
    cursor.execute("SELECT * FROM tbl_users WHERE uname=? AND user_level=? AND passw=? LIMIT 10",(username,level,password))

    row=cursor.fetchone()
    if row:
        return 'SUCCESS'+str(row[0])
    else:
        return "Invalid Details Entered Please retry..."
