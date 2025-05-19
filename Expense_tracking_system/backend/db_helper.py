import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")



@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary = True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense) 
        


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit = True) as  cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", 
                       (expense_date, amount, category, notes))


def delete_expenses_for_expense_date(expense_date):
    logger.info(f"delete_expenses_for_expense_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_summary_expenses(start_date, end_date):
    logger.info(f"fetch_summary_expenses called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, sum(amount) as total FROM expenses 
                       where expense_date BETWEEN %s AND %s 
                       GROUP BY category''', (start_date, end_date))
        expenses = cursor.fetchall()
        return expenses
    

def fetch_summary_expenses_monthly():
    logger.info(f"fetch_summary_expeses_monthly")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT 
                       MONTHNAME(expense_date) AS 'month_name', 
                       SUM(amount) AS total 
                       FROM expenses
                       GROUP BY MONTHNAME(expense_date)
                       ORDER BY MONTHNAME(expense_date) asc''')
        expenses = cursor.fetchall()
        return expenses
        




if __name__ == "__main__":
    # Your code here must be indented
    summary = fetch_summary_expenses_monthly()
    print(summary)