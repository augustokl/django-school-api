from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(
                serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationsViewSet(viewsets.ModelViewSet):
    """Show all registration"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(RegistrationsViewSet, self).dispatch(*args, **kwargs)


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
