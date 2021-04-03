import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from school.models import Course, Student

def create_student(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cpf = cpf.generate()
        birthday = fake.date_between(start_date='-18y', end_date='today')
        a = Student(name=name,rg=rg, cpf=cpf,birthday=birthday)
        a.save()

def create_course(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        code = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(code=code, description=description, level=level)
        c.save()


create_student(200)
create_course(5)