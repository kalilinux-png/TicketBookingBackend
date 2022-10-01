import uvicorn 
from fastapi import FastAPI
from database import Database
from fastapi.requests import Request
import json
import sqlite3

app = FastAPI(debug=False)
db = Database("test.db")

@app.get("/")
def greet():
    return "Namaste \n Server Status:Online"

@app.post("/upload/user_data/")
async def add_user_data(request:Request):
    """Function Used To Add User Data In Database"""
    user_data =await  request.body()
    user_data = json.loads(user_data.decode("utf-8"))
    print("request body",user_data)
    raw_string = f"INSERT INTO ORDERBOOK (NAME,MOVNAME,PRICE,SEATS) VALUES ('{user_data['name']}','{user_data['movname']}', '{user_data['price']}','{user_data['seats']}' );"
    print("raw_string",raw_string)
    try:
        db_response = db.execute_command(raw_string)
        return {"Status":"OK","Message":"User Successfully Added To Database"}
    except Exception as error:
        return {"Status":"Fail","Message":"Exception Occured",'error':error}

if __name__=="__main__":
    uvicorn.run(app=app)