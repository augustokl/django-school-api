from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birthday = models.DateField()
    celphone = models.CharField(max_length=11, default='')
    perfil_image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    level = models.CharField(
        max_length=1, choices=LEVEL, blank=False, default='B')

    def __str__(self):
        return self.description


class Registration(models.Model):
    TIME_COURSE = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_course = models.CharField(
        max_length=1, choices=TIME_COURSE, blank=False, default='M')
