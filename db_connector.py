import pymysql

schema_name = "mydb"

def add_user(user_id, username):
    print("attempting to connect to 1db")
    schema_name = 'users'
    # Establishing a connection to DB
    try:
        print("attempting to connect to db")
        conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()

         # Inserting data into table
        statementToExecute = "CREATE TABLE `" + schema_name + ("`.`users`(`user_id`PRIMARY KEY, INT, NOT NULL,"
                                                               "`user_name` VARCHAR(50), NOT NULL,'CREATION "
                                                               "_DATE'VARCHAR(50);")

        cursor.close()
        conn.close()
    except:
        print("can not connect to database")






