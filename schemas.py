from pydantic import BaseModel
from datetime import date
from enum import Enum


class LeaveType(Enum):
    ANNUAL = 'annual'
    SICK = 'sick'
    PERSONAL = 'personal'

class LeaveStatus(Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECT = 'reject'


class LeaveSchema(BaseModel):
    employee_id: str
    start_date:  date
    end_date: date
    leave_type: LeaveType
    reason: str


class LeaveResponseSchema(LeaveSchema):
    id: int
    working_days: int
    status: LeaveStatus

