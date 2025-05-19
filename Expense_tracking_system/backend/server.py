from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

class MonthlyAnalytics(BaseModel):
    month_name: str 
    total: float


@app.get("/expenses/{expense_date}", response_model = List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_expense_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
        
    return {"message: Epenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_summary_expenses(date_range.start_date, date_range.end_date)

    if data is None:
        raise HTTPException(status_code =500, details = "Failed to retrieve expense summary from the database")
    
    total = round(sum([row["total"] for row in data]),2)

    breakdown = {}
    for row in data:
        percentage = round((row["total"] / total) * 100,2) if total != 0 else 0
        breakdown[row["category"]] = {
            "total": row["total"],
            "percentage":percentage
        }
    return breakdown

#{
 #   "Rent": {"total": 1234, "percentage": 34.5},
 #   "Shopping": {"total": 3524, "percentage": 50}
#}


@app.get("/analytics/monthly/", response_model=List[MonthlyAnalytics]) 
def get_analytics_monthly():
    """
    Get monthly expense totals
    Returns:
        List of monthly analytics with month name and total amount
        Example: [{"month_name": "January", "total": 1500.50}, ...]
    """
    return db_helper.fetch_summary_expenses_monthly()

