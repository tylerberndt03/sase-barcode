import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
#import google.auth
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
import gspread
from oa


class Base(DeclarativeBase):
    pass

class Member(Base):
    __tablename__ = "members"

    barcode_id: Mapped[int] = mapped_column(primary_key=True)
    ufid: Mapped[int]
    name: Mapped[str]
    major: Mapped[str]

    def __repr__(self) -> str:
        return f"Member(barcode_id={self.barcode_id!r}, ufid={self.ufid!r}, name={self.name!r}, major={self.major!r})"

def AcquireFromDB(barcode_id) -> Member:
    pass

def AddToSheet(member: Member, sheet: gspread.Worksheet):
    newRow = [Member.ufid, Member.name, Member.major]
    sheet.append_row(newRow)

