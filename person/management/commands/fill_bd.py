from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from decimal import Decimal
import random
from progress.bar import IncrementalBar

from person.models import Department, Employee


FILL_COUNT = 50000

fake = Faker()


def create_department(parent=None, level=0):
    if level == 5:
        return
    for _ in range(random.randint(1, 5)):
        department = Department.objects.create(
            name=fake.company(),
            parent=parent
        )
        create_department(parent=department, level=level+1)


def create_employee(department):
    full_name = fake.name()
    position = fake.job()
    hire_date = fake.date_between(start_date='-10y', end_date='today')
    salary = Decimal(random.randint(30000, 100000))
    Employee.objects.create(
        full_name=full_name,
        position=position,
        hire_date=hire_date,
        salary=salary,
        department=department
    )


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **options):
        with transaction.atomic():
            Department.objects.all().delete()
            Employee.objects.all().delete()

            root_department = Department.objects.create(name='Headquarters')
            create_department(parent=root_department)

            departments = Department.objects.all()

            bar = IncrementalBar('Заполнено', max=FILL_COUNT)
            for _ in range(FILL_COUNT):
                bar.next()
                department = random.choice(departments)
                create_employee(department)
            bar.finish()

        self.stdout.write(
            self.style.SUCCESS('База данных успешно заполнена')
        )
