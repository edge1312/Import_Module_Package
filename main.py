from application.salary import calculate_salary as cal_sal
from db.people import get_employees as get_em
from datetime import datetime


def logger(func):
    def write_log():
        logfile_name = 'log.txt'
        with open(logfile_name, 'a', encoding='utf-8') as file:
            file.write(f'Function {func} was called at: {str(datetime.now())}\n')
        func()
    return write_log


cal_sal = logger(cal_sal)
get_em = logger(get_em)



if __name__ == "__main__":
    cal_sal()
    get_em()
    print('Program finished at:', datetime.now())



