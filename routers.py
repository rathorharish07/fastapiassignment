# from fastapi import APIRouter, Depends
# from typing import List
# from schemas import LeaveResponseSchema, LeaveSchema
# myrouter = APIRouter()

# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.orm import sessionmaker, Session, declarative_base
# import sqlalchemy


# # set up database SQLITE
# DATABASE_URL = 'sqlite:///./test.db'
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# Base.metadata.create_all(bind=engine)

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Database model
# class LeaveRequest(Base):
#     __tablename__ = 'leave'
#     id = Column(Integer, primary_key=True, index=True)
#     employee_id = Column(String, index=True)
#     start_date= Column(String)
#     end_date= Column(String)
#     leave_type= Column(String)
#     reason= Column(String)


# myrouter.post("/leave-request/", response_model=LeaveResponseSchema)
# async def create_leave_request(
#     leave_request_data: LeaveSchema,
#     db: Session = Depends(get_db)
# ):
#     db_item = LeaveRequest(**leave_request_data.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item