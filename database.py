import sqlite3

class Database:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn =  sqlite3.connect(db_name)


    def connect_db(self,db_name):
        """Function Used To Connect With Database"""
        self.conn=  sqlite3.connect(db_name)

    def execute_command(self,command):
        """Function Used To Execute Any Database Query
        ARGS: COMMAND:str
        RETURN : CURSOR:tuple"""
        if not self.conn:
            return "Please Connect With Database First Use Method connect_db"
        output = self.conn.execute(command)
        self.conn.commit()
        return output
    def insert_data():
        """Function Used To Insert User Data In Database"""
        
        
if __name__=="__main__":
    db = Database('test.db')
    # uncomment if you have not created the table
    # db.execute_command('''CREATE TABLE ORDERBOOK
    #      (ID INT AUTO_INCREMENT ,
    #      NAME           TEXT    NOT NULL,
    #      MOVNAME            CHAR(50)     NOT NULL,
    #      PRICE        INT,
    #      SEATS         INT NOT NULL);''')
    output = db.execute_command('''INSERT INTO ORDERBOOK (NAME,MOVNAME,PRICE,SEATS) \
      VALUES ('shubham', 32, 'California', 20000.00 )''')
    output = db.execute_command('''SELECT * FROM ORDERBOOK''')
    for k in output:
        print(k)

