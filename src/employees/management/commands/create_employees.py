import random

from django.core.management.base import BaseCommand
from faker import Faker

from src.employees.models import Department, Employee

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = 'Fill the database with fake data'

    def create_department_hierarchy(self, parent_department, level):
        if level == 6:
            return
        departments = []
        for _ in range(2):
            department = Department.objects.create(
                name=fake.company(),
                parent=parent_department,
            )
            departments.append(department)
        for department in departments:
            self.create_department_hierarchy(department, level + 1)

    def handle(self, *args, **options):
        # Создаем корневое подразделение
        root_department = Department.objects.create(
            name='Company',
            parent=None,
        )

        # Создаем структуру подразделений до 5 уровней
        self.create_department_hierarchy(root_department, level=1)
        self.stdout.write(self.style.SUCCESS('Созданы подразделения.'))

        # Создаем более 50 000 сотрудников
        total_employees = 50000
        batch_size = 4000
        employees = []
        for c_employees in range(total_employees):
            department = random.choice(Department.objects.all())
            employee = Employee(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
                salary=random.randint(30000, 150000),
                department=department,
            )
            employees.append(employee)
            if len(employees) == batch_size:
                Employee.objects.bulk_create(employees)
                employees = []
                self.stdout.write(self.style.SUCCESS(f'Созданы {c_employees + 1} работников'))

        # Последние оставшиеся объекты
        if employees:
            Employee.objects.bulk_create(employees)

        self.stdout.write(self.style.SUCCESS('Успешно созданы подразделения и работники'))
