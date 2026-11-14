import csv
import json
import os
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'employees.csv'
OUTPUT_DIR = BASE_DIR / 'output'


def log(message):
    with (OUTPUT_DIR / 'log.txt').open('a', encoding='utf-8') as file:
        file.write(f'{datetime.now().isoformat()} - {message}\n')


def check_paths():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.is_file():
        print('Error: data/employees.csv was not found.')
        log('Input CSV file was not found.')
        return False
    print(f'CSV absolute path: {DATA_FILE.resolve()}')
    return True


def backup_file(src, dst):
    line_count = 0
    with src.open('r', encoding='utf-8', newline='') as source, dst.open('w', encoding='utf-8', newline='') as destination:
        for line in source:
            destination.write(line)
            line_count += 1
    return line_count


def create_lock():
    try:
        with (OUTPUT_DIR / 'lock.txt').open('x', encoding='utf-8') as file:
            file.write(datetime.now().isoformat())
        print('Lock file created.')
    except FileExistsError:
        print('Report already exists.')


def inspect_csv():
    with DATA_FILE.open('r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    print('CSV header:', header)
    print('First 3 employees:')
    for row in rows[:3]:
        print(row)
    print('Employee records:', len(rows))


def load_employees():
    with DATA_FILE.open('r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def analyze_employees(employees):
    department_counts = Counter()
    salary_totals = Counter()
    active_employees = []
    for employee in employees:
        department = employee['department']
        salary = int(employee['salary'])
        department_counts[department] += 1
        salary_totals[department] += salary
        if employee['is_active'] == 'True':
            active_employees.append(employee)
    stats = [
        {'department': department, 'employee_count': count,
         'avg_salary': round(salary_totals[department] / count, 2)}
        for department, count in department_counts.items()
    ]
    stats.sort(key=lambda item: item['avg_salary'], reverse=True)
    print('Department statistics:')
    for item in stats:
        print(f"{item['department']}: {item['employee_count']} employees, average salary {item['avg_salary']:.2f}")
    top_three = sorted(active_employees, key=lambda item: int(item['salary']), reverse=True)[:3]
    print('Top 3 active earners:')
    for employee in top_three:
        print(f"{employee['first_name']} {employee['last_name']}: {employee['salary']}")
    print(f'Active employees: {len(active_employees)}')
    print(f'Inactive employees: {len(employees) - len(active_employees)}')
    return stats, active_employees


def write_department_stats(stats):
    with (OUTPUT_DIR / 'department_stats.csv').open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['department', 'employee_count', 'avg_salary'])
        writer.writeheader()
        writer.writerows(stats)


def write_high_earners(active_employees):
    rows = [
        [employee['id'], f"{employee['first_name']} {employee['last_name']}", employee['department'], employee['salary']]
        for employee in active_employees if int(employee['salary']) >= 5000
    ]
    with (OUTPUT_DIR / 'high_earners.csv').open('w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'full_name', 'department', 'salary'])
        writer.writerows(rows)
    print(f'High earners saved: {len(rows)}')




# ვერ მოვრჩი ბოლომდე რავი 
