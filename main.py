import os
import uvicorn
from fastapi.templating import Jinja2Templates  # for templating purpose
from fastapi.staticfiles import StaticFiles  # for unknown purpose
from fastapi import FastAPI
from database import Database
from fastapi.requests import Request
import json
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app = FastAPI()
app.mount("/templates",StaticFiles(directory='templates'),name='static')
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_methods = ["*"],allow_headers=["*"],allow_credentials=True)
db = Database("test.db")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def greet():
    return "Namaste \n Server Status:Online"


@app.get("/test")
def test():
    return "test working"


@app.post(
    "/upload/user_data/"
)  # endpoint to recieve user data from front end: data from front end must in body
async def add_user_data(request: Request):
    """Function Used To Add User Data In Database"""
    user_data = await request.body()
    user_data = json.loads(user_data.decode("utf-8"))
    print("request body", user_data)
    # raw_string = f"INSERT INTO ORDERBOOK (date,movie_name,theather_name,place_name,no_of_seats_value,type_of_food_name,time_value,dimension_name) VALUES ('{user_data['date']}','{user_data['movie_name']}', '{user_data['theather_name']}','{user_data['place_name']}','{user_data['no_of_seats_value']}','{user_data['type_of_food_name']}','{user_data['time_value']}','{user_data['dimension_name']}' );" #sql query to insert data in already created order table
    # try:
        # db_response = db.execute_command(raw_string)
    # except Exception as error:
        # print("Exception Occured",error)
    return templates.TemplateResponse(
        "ticket.html",
        {
            "request": request,
            "time": user_data["time_value"],
            "no_of_seats": user_data["no_of_seats_value"],
            "movie_name": user_data["movie_name"],
            "location": user_data["place_name"],
            "theather": user_data["theather_name"],
        },
    )

@app.get("/db_values")
def get_db():
    """Function Used To Return All Data Stored In Database"""
    try:
        db_output = db.execute_command("SELECT * FROM ORDERBOOK")
        print("db output",db_output)
        return {"Message":"Success","Data":list(db_output)}
    except Exception as error:
        db_output = error
        print("db output as error",db_output)
        return {"Message":"Error","Error":error}
    
    
if __name__ == "__main__":
    os.system(
        "python -m uvicorn main:app --reload --port 5000"
    )  # this will start a local server on port 5000
