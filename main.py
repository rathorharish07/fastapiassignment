from datetime import date
import datetime

from fastapi import Path, Depends
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from pydantic import BaseModel
from typing import List

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import sqlalchemy

from schemas import LeaveResponseSchema, LeaveSchema, LeaveStatus
from utils import find_working_days

# create app
app = FastAPI()

# app.include_router(myrouter)
# set up database SQLITE
DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# create table
class LeaveRequest(Base):
    __tablename__ = 'leave'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, index=True)
    start_date= Column(String)
    end_date= Column(String)
    leave_type= Column(String)
    working_days = Column(Integer)
    reason= Column(String)
    status = Column(String)

# bind engine
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/leave-request/", response_model=LeaveResponseSchema)
async def create_leave_request(
    leave_request_data: LeaveSchema,
    db: Session = Depends(get_db)
):
    # validate start and end date
    if not leave_request_data.start_date <= leave_request_data.end_date:
        raise RequestValidationError("end date cannot be earlier than start date")

    db_item = LeaveRequest(**leave_request_data.dict())
    # add working days
    db_item.working_days = find_working_days(leave_request_data.start_date, leave_request_data.end_date)
    db_item.leave_type = db_item.leave_type.value
    # mark intially pending
    db_item.status = LeaveStatus.PENDING.value
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/leave-request/{employee_id}", response_model=List[LeaveResponseSchema])
async def create_leave_request(
    employee_id: str = Path(),
    db: Session = Depends(get_db)
):
    response = db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id)
    return response



