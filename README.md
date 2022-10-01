#Installation

1.pip install -r requirements.txt

2. Run command to create table

```
conn.execute('''CREATE TABLE ORDERBOOK
         (ID INT PRIMARY KEY     AUTOINCREMENT NOT NULL,
         NAME           TEXT    NOT NULL,
         MOVNAME            CHAR(50)     NOT NULL,
         PRICE        INT,
         SEATS         INT NOT NULL);''')
conn.commit()
conn.close()
```
