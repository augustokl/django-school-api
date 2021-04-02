from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
  list_display = ('id', 'name', 'rg', 'cpf', 'birthday')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 20

class Courses(admin.ModelAdmin):
  list_display = ('id', 'code', 'description')
  list_display_links = ('id', 'code')
  search_fields = ('description',)
  list_per_page = 20

admin.site.register(Student, Students)
admin.site.register(Course, Courses)
