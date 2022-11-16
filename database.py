import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name,check_same_thread=False)

    def connect_db(self, db_name):
        """Function Used To Connect With Database"""
        self.conn = sqlite3.connect(db_name)

    def execute_command(self, command):
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


if __name__ == "__main__":
    db = Database("test.db")
    # uncomment if you have not created the table
    try:
        db.execute_command(
            """CREATE TABLE ORDERBOOK
            (ID INT AUTO_INCREMENT ,
            date TEXT NOT NULL,
            movie_name            CHAR(50)     NOT NULL,
            theather_name TEXT NOT NULL,
            place_name CHAR(50) NOT NULL,
            no_of_seats_value   INT NOT NULL,
            type_of_food_name TEXT NOT NULL,
            time_value TEXT NOT NULL,
            dimension_name TEXT NOT NULL );"""
        )
    except Exception as Error:
        print("Exception Handled", Error)
    # output = db.execute_command('''INSERT INTO ORDERBOOK (NAME,MOVNAME,PRICE,SEATS) \
    #   VALUES ('shubham', 32, 'California', 20000.00 )''')
    output = db.execute_command("SELECT * FROM ORDERBOO")
    for k in output:
        print(k)
