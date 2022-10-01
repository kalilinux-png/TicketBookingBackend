'''Module Use To Run Project In Serial'''
import os

if __name__=="__main__":
    os.system("cd venv\Scripts && activate") # navigate to the venv folder
    os.system("pip install -r requirements.txt") # install all the required modules
    os.system("python database.py") # Create Datbase and table
    os.system("python main.py") # Open Up the localhost server 