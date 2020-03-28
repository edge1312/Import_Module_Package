from application.salary import calculate_salary as cal_sal
from db.people import get_employees as get_em
from datetime import datetime


if __name__ == "__main__":
    cal_sal()
    get_em()
    print(datetime.now())