from rest_framework import serializers
from school.models import Course, Student, Registration

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'rg', 'cpf', 'birthday']

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    exclude = []

class ListRegistrationSerializer(serializers.ModelSerializer):
  course = serializers.ReadOnlyField(source='course.description')
  time_course = serializers.SerializerMethodField()

  class Meta:
    model = Registration
    fields = ['course', 'time_course']

  def get_time_course(self, object):
    return object.get_time_course_display()

class ListCourseStudentsSerializer(serializers.ModelSerializer):
  student = serializers.ReadOnlyField(source='student.name')

  class Meta:
    model = Registration
    fields = ['student']

  def get_time_course(self, object):
    return object.get_time_course_display()

  
class StudentSerializerV2(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'rg', 'cpf', 'birthday', 'celphone']

