from rest_framework import viewsets, generics
from school.models import Course, Student, Registration
from school.serializers import CourseSerializer, StudentSerializer, \
    RegistrationSerializer, ListRegistrationSerializer, \
    ListCourseStudentsSerializer, StudentSerializerV2


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2

        return StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    """Show all registration"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationsViewSet(generics.ListAPIView):
    """List student registrations"""
    serializer_class = ListRegistrationSerializer

    def get_queryset(self):
        queryset = Registration.objects.filter(student=self.kwargs['pk'])
        return queryset


class ListCourseStudentsViewSet(generics.ListAPIView):
    """List course students"""
    serializer_class = ListCourseStudentsSerializer

    def get_queryset(self):
        queryset = Registration.objects.filter(course=self.kwargs['pk'])
        return queryset
