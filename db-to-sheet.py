# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy import select
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
#import google.auth
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
import gspread
import mysql.connector
from mysql.connector.cursor import MySQLCursor
#from oa

class DBToSheet:
    def __init__(self, eventSheet: str):
        gc = gspread.service_account() # This will connect to a set drive or something
        self.memberSheet = gc.open("Members") # or whatever it's called
        self.eventSheet = gc.open(eventSheet)
    
    def dbToSheet(self, barcode_id: int):
    #newRow = [Member.ufid, Member.name, Member.major]
        row = self.memberSheet.col_values(1).index(barcode_id) + 1
        member = self.memberSheet.row_values
        self.eventSheet.append_row(member)




# class Member():
#     barcode_id: int
#     ufid: int
#     name: str
#     major: str

# def AcquireFromDB(barcode_id: int, cursor: MySQLCursor) -> list:
#     query = "SELECT * FROM members WHERE barcode_id = %s"
#     cursor.execute(query, [barcode_id])
#     toAdd = cursor.fetchone()
#     return list(toAdd)



# def main():
    # db = mysql.connector.connect(
    #     host = "localhost",
    #     user = "root",
    #     password = "sase-test",
    #     database = "members"
    # )
    # cursor = db.cursor()
    
    # testList = AcquireFromDB(0, cursor)
    # print(testList)

def __init__():
    gc = gspread.service_account() # This will connect to a set drive or something



# if __name__ == "__main__":
#     main()




