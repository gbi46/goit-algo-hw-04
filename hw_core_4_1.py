import pathlib
from data import load_data, clean_data
from collections import namedtuple

def get_salaries(data)-> list[int]:
    salaries = list()
    
    for salary in data:
        clean_salary = int(salary.split(',')[1])
        salaries.append(clean_salary)

    return salaries

def total_salary(path):
    file_data = load_data(path)
    data = clean_data(file_data)

    salaries = get_salaries(data)

    total_salary = sum(salaries)
    avg_salary = total_salary // len(salaries)

    SalaryData = namedtuple("SalaryData", ['total', 'average'])

    return SalaryData(total=total_salary, average=avg_salary)

curr_dir = pathlib.Path(__file__).parent
file_path = curr_dir / "monthly_developers_salaries.txt"

total, average = total_salary(file_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
