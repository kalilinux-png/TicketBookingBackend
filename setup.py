'''Module Use To Run Project In Serial'''
import os

if __name__=="__main__":
    os.system("cd venv\Scripts && activate")
    os.system("pip install -r requirements.txt")
    os.system("python database.py")
    os.system("python main.py")